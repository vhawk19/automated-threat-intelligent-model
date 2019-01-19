#Main program; does all web scraping, parsing, formatting; is called by 'DailyRun.py'

#Necessary Imports
import csv
import urllib.request
from io import BytesIO
from zipfile import ZipFile
from datetime import datetime
import sys


#Function to check repeated intel
def check_repeats(intel, i_type, ips, domains, urls, sha1):
    if i_type == 'IP':         #Separate sets for each intel type to improve efficiency
        length = len(ips)
        ips.add(intel)
        if len(ips)> length:   #Add intel to set, see if set size increases; if it doesn't, the intel is a repeat
            return True
        else:
            return False
    elif i_type == 'DOMAINS' or i_type == 'DNS':
        length = len(domains)
        domains.add(intel)
        if len(domains) > length:
            return True
        else:
            return False
    elif i_type == 'URLS':
        length = len(urls)
        urls.add(intel)
        if len(urls) > length:
            return True
        else:
            return False
    elif i_type == 'SHA-1':
        length = len(sha1)
        sha1.add(intel)
        if len(sha1) > length:
            return True
        else:
            return False
    else:
        return True
        



#Main function, called by 'DailyRun.py', returns counter variable with total number of intel processed
def bro_generator(newpath):
    
    errors=[]  #Stores all errors encountered so they can be analyzed later and the program doesn't crash
    
    try:
        sources = open('sources.txt', 'r')  #Note: this contains direct links to the intel files from each source
    except FileNotFoundError:
        errors.append("sources.txt does not exist")
        return 0


    output = open(newpath + '/formatted-intel.txt','w')  #Formatted intel
    error_log = open(newpath + '/errors-log.txt','w')    #Log with all error messages
    repeats_log = open(newpath + '/repeats-log.txt','w') #Log with all repeated intel

    intel_type = {'IP' : '::ADDR' , 'DOMAINS' : '::DOMAIN' , 'URLS' : 'URL' , 'SHA-1' : '::CERT_HASH', 'DNS' : 'DOMAINS', 'SUBNET': 'SUBNET', 'EMAIL': 'EMAIL', 'USERNAME': 'USER_NAME', 'MD5': 'PUBKEY_HASH'}  #for indicator_type
    src_info = sources.read().splitlines()  #for meta.source and url

    counter = 0    #To count intel analyzed

    #Sets to store intel, used to check for repeats
    ips = set([])
    domains = set([])
    urls = set([])
    sha1 = set ([]) 
    repeats=[]  #Stores all repeated intel

    output.write("#fields indicator    indicator_type    meta.source    meta.desc    meta.url") #Header for data
    
    src_info = src_info [1: ]   #Gets rid of first line of 'sources.txt', which is the path to the Logs directory
    
    for source in src_info:

        try:
            
            if source !="" and source[0]!= '#':  #Ensure blank lines aren't read, sources can be commented out

                source=source.split()


                #These sources are all plaintext txts with minimal metadata
                if (source[0].upper() in ['SNORT', 'TALOS', 'ET_IPS', 'MALIPS', 'CIARMY', 'MALHOSTS']) or (source[0] == 'Abuse'):
                    try:
                        raw_data = urllib.request.urlopen(source[1])  #Opens url of source
                    except:
                        errors.append(source[0]+ " does not have a valid link to intel")
                        data=[]  #If url is unreachable, this source is not processed

                    try:    
                        data = raw_data.read().decode('utf-8').splitlines()  #Reads full source
                    except:
                        errors.append(source[0]+ " does not link directly to the intel file")
                        data=[]  #If url does not lead to readable intel, this source is not processed 
                        
                    for r in data:
                        try:
                            if r != "" and r[0]!='#':
                                if source[0].upper() == 'MALHOSTS':  #This source contains extra unneeded data
                                    r = r.split()[-1]
                                if r!= 'localhost':  #Can't add 'localhost' as a malicious domain
                                    if check_repeats(r, source[2].upper(), ips, domains, urls, sha1):  #Check if intel is repeated
                                        line = [r, intel_type[source[2].upper()], source[0],  '-', source[1]]  #Formatted line to add to output text, dash is used because there is no desc metadata
                                        counter = counter+1
                                        output.write ('    '.join(line)+ '\n')  #\t was not consistent, replaced with literal tab
                                    else:
                                        repeats.append(r)
                        except:
                            errors.append(source[0] + " contains invalid intel")  #If intel line is not able to be processed, then this source contains some invalid intel (ex. uncommented non-intel text)
        

                #This source is a csv with meta.desc metadata
                elif source[0] == 'abuse':
                    try:
                        raw_data = urllib.request.urlopen(source[1])
                    except:
                        errors.append(source[0]+ " does not have a valid link to intel")
                        data=[]

                    try:    
                        data = raw_data.read().decode('utf-8').splitlines()
                    except:
                        errors.append(source[0]+ " does not link directly to the intel file")
                        data=[]
                    
                    for r in data:
                        try:                
                            if r[0]!='#':
                                intel = r[r.find(',')+1: ].split(',')  #This source contains intel and description metadata
                                if check_repeats(intel[0], source[2].upper(), ips, domains, urls, sha1):
                                    line = [intel[0], intel_type[source[2].upper()], source[0], intel[1], source[1]]
                                    counter = counter+1
                                    output.write ('    '.join(line) + '\n' )
                                else:
                                    repeats.append(intel[0])
                        
                        except:
                            errors.append(source[0] + " contains invalid intel")

           
                #This source's url leads to downloaded large zip files containing csv intel
                elif source[0] == 'Blacklist':
                    try:
                        raw_data = urllib.request.urlopen(source[1])
                    except:
                        errors.append(source[0]+ " does not have a valid link to intel")

                    try:
                        with ZipFile(BytesIO(raw_data.read())) as my_zip_file:  #To read zip file
                            for contained_file in my_zip_file.namelist():
                                # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
                                for line in my_zip_file.open(contained_file).readlines():
                                    try:
                                        d_line = line.decode('utf-8')  #Decoded line from source (originally raw text)
                                        d_line=d_line.replace('\n','')
                                        
                                        if check_repeats(d_line, source[2].upper(), ips, domains, urls, sha1):
                                            line = [d_line, intel_type[source[2].upper()], source[0],  '-', source[1]]
                                            counter = counter+1
                                            output.write ('    '.join(line) + '\n')
                                        else:
                                            repeats.append(d_line)
                                    except:
                                        errors.append(source[0] + " contains invalid intel")
                    except:
                        errors.append(source[0]+ " does not link directly to the intel file")


                #These sources are plaintext, but are very formatted, contain intel, desc metadata, and extra unneeded data
                elif source[0].upper() in ['BOTCC', 'TOR']:
                    try:
                        raw_data = urllib.request.urlopen(source[1])
                    except:
                        errors.append(source[0]+ " does not have a valid link to intel")

                    try:    
                        data = raw_data.read().decode('utf-8').splitlines()
                    except:
                        errors.append(source[0]+ " does not link directly to the intel file")
                        data=[]
                        
                    
                    for r in data:
                        try:                
                            if r != "" and r[0]!='#':
                                addresses = r[r.find('[')+1: r.find(']')].split(',')
                                if 'msg' in r:  #meta.desc is contained in the msg field of each line in the source
                                    msg = r[r.find('msg')+5: r.find(';')-1] #To extract the msg from the formatting
                                else:
                                    msg = "-"
                                    
                                for address in addresses:
                                    if check_repeats(address, source[2].upper(), ips, domains, urls, sha1):
                                        line = [address, intel_type[source[2].upper()], source[0], msg, source[1]]
                                        counter = counter+1
                                        output.write ('    '.join(line) + '\n' )
                                    else:
                                        repeats.append(address)
                        
                        except:
                            errors.append(source[0] + " contains invalid intel")


                #This source url leads to a downloaded, non-zip file with plaintext intel
                elif source[0].upper() == 'ALIENVAULT':
                    try:
                        raw_data = urllib.request.urlopen(source[1])
                    except:
                        errors.append(source[0]+ " does not have a valid link to intel")

                    try:    
                        data = raw_data.read().decode('utf-8').splitlines()
                    except:
                        errors.append(source[0]+ " does not link directly to the intel file")
                        data=[]
                        
                    
                    for r in data:
                        try:                
                            if r!= "" and r[0]!='#':
                                intel = r.split(" # ")  #Each line in the source contains the intel and desc metadata
                                if check_repeats(intel[0], source[2].upper(), ips, domains, urls, sha1):
                                    line = [intel[0], intel_type[source[2].upper()], source[0], intel[1], source[1]]
                                    counter = counter+1
                                    output.write ('    '.join(line) + '\n' )
                                else:
                                    repeats.append(intel[0])
                        
                        except:
                            errors.append(source[0] + " contains invalid intel")    

        except:
            errors.append('Unknown error in ' + source)
        
    output.close()
    repeats_log.write("Repeated intel: \n" + '\n'.join(repeats))
    repeats_log.close()
    error_log.write("Errors encountered: \n" + '\n'.join(errors))
    error_log.close()
    return counter

