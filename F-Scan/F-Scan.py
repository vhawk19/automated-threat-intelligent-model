#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import os.path
import csv
import time
from functools import reduce
import re
#import json
from os import path
from colorama import Back, Fore, init, Style
from time import sleep
from tqdm import tqdm


def almacenardatos():
    """a='c'
    print('s')
    return a"""
    init()
    print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
    init()
    print(Fore.RED + "Coincidencias de (port) o puertos encontrados "+Fore.GREEN+" **************************************")
    print ("")
    RED = '\033[1;31m'
    NOCOLOR = '\033[0;0m'

    palabras4 = ['tcp', '.com', 'n/a']

    palabra4 = 'tcp'
    ocurrencias4 = []
    with open('doc.txt') as lineas:
        for linea in lineas:
            if palabra4 in linea:
                ocurrencias4.append(linea)

    
        #print(aImprimir4)
    return ocurrencias4

def crear_archivo():
    if path.exists('prueba1.txt'):
        print('El archivo ya existe')
        file=open("prueba1.txt", "a")
    else:
        file=open("prueba1.txt", "a")
        print('El archivo fue creado')

        pass    

def menu():

    """
Inicio logo         ###################################################################
    """


print ("""
#######          #####   #####     #    #     #
#               #     # #     #   # #   ##    #
#               #       #        #   #  # #   #
#####     ####   #####  #       #     # #  #  #
#                     # #       ####### #   # #
#               #     # #     # #     # #    ##
#                #####   #####  #     # #     #
""")                                                                  

print(Fore.RED + "    --------------------------------------------         ")            
print (Fore.GREEN +"        By Kai Iyer  | v 0.1                         \n")


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Enter an option: "))
            correcto=True
        except ValueError:
            print('Error, enter an option')
            print ("")
     
    return num
 
salir = False
opcion = 0

while not salir:

    print(Fore.RED + "1. "+Fore.WHITE+" Search vulnerabilities ")
    init()
    print(Fore.RED + "2. "+Fore.WHITE+" Search for open ports  ")
    init()
    print(Fore.RED + "3. "+Fore.WHITE+" Search public emails   ")
    init()
    print(Fore.RED + "4. "+Fore.WHITE+" Show information found")
    init()
    print(Fore.RED + "5. "+Fore.WHITE+" Details of F-Scan")
    init()
    print(Fore.RED + "6. "+Fore.WHITE+" Exit")
    print ("") 
    print ("Choose an option")
    print ("") 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:

        ############################################################################################################
        
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analyze with T.rex\n\n")
        url_analyze = raw_input('Enter the URL to analyze, for example: www.mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")    

        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" The script is working, this process can take from 3 to 10 minutes depending " +Fore.GREEN+ " on your internet speed and the information found by " +Fore.WHITE+ "T.rex_Scan\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Better go and have a coffee while the information collection process finishes, the script will go back to the main menu when the scan finishes. " +Fore.GREEN+ "" +Fore.WHITE+ "")
        print("")
        init()
        print(Fore.RED + "   ( ( "+Fore.WHITE+"")
        init()
        print(Fore.RED + "    ) ) "+Fore.WHITE+"")
        init()
        print(Fore.RED + "  ........"+Fore.WHITE+"")
        init()
        print(Fore.RED + "  |      |]"+Fore.WHITE+"  go!! ")
        init()
        print(Fore.RED + "  \      / "+Fore.WHITE+"  and have   ")
        init()
        print(Fore.RED + "   `----'"+Fore.WHITE+"    a coffee   ")
        print("")

        
        #os.system("gnome-terminal -e 'ping 8.8.8.8'")
        #command = '  nslookup ' + url_analyze +  ' > scan_ip.txt '

        #os.system(command)

        command = '  whatweb -v  ' + url_analyze +  ' > scan_version.txt --color never'

        os.system(command)

        command = '  wpscan --url ' + url_analyze +  ' --enumerate p > scan_page.txt --batch --no-color --no-banner'

        os.system(command)
    
        for i in tqdm(range(100)):
            sleep(0.02) 
        print("") 

        init()
        print(Fore.RED + "[*]"+Fore.GREEN+" Finished analysis }:) \n\n")
        print ("")
        time.sleep(5)
        os.system('clear')
        
    elif opcion == 2:

        ############################################################################################################
        
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analyze with T.rex\n\n")
        ports_analyze = raw_input('Enter the URL to analyze, for example: www.mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("") 
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Starting" +Fore.GREEN+ " port analysis" +Fore.WHITE+ ", this may take several minutes, please wait\n")
        print("")
        init()
        print(Fore.GREEN + " ¯\_(ツ)_/¯ "+Fore.WHITE+" While T.rex_scan scans the ports visit our website www.networkiscolombia.com ")
        print("")
        

        command = 'nmap -O -sS ' + ports_analyze +  ' > scan_ports.txt'
        
        os.system(command) 

        for i in tqdm(range(100)):
            sleep(0.02) 
        print("") 

        init()
        print(Fore.RED + "[*]"+Fore.GREEN+" Finished analysis }:) \n\n")
        print ("")
        time.sleep(5)
        os.system('clear')

    elif opcion == 3:

        ############################################################################################################
        
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analyze with T.rex\n\n")
        url_analyze_mail = raw_input('Enter the email domain to analyze, example: mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("") 
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Starting" +Fore.GREEN+ " mail search" +Fore.WHITE+ ", this may take several minutes, please wait\n")
        print("")
        init()
        print(Fore.GREEN + " ¯\_(ツ)_/¯ "+Fore.WHITE+" Remember that corporate emails are a big security hole for companies ")
        print("")

        command = 'theharvester -d ' + url_analyze_mail +  ' -l 500 -b all > scan_mails.txt '
        os.system(command)
        
        for i in tqdm(range(100)):
            sleep(0.02) 
        print("") 

        init()
        print(Fore.RED + "[*]"+Fore.GREEN+" Finished analysis }:) \n\n")
        print ("")
        time.sleep(5)
        os.system('clear')
       
        


        #########################################################################################
    elif opcion == 4:
        
        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Vulnerabilities found (CVE)\n")

        imp_cve = open('scan_page.txt','r')

        #[for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        #[0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto 

        regex = '[CVE]+-[0-9]+-[0-9]+'

        list_cve = []

        for line2 in imp_cve:
            line2 = line2.rstrip()
            y = re.findall('[CVE]+-[0-9]+-[0-9]+', line2)
            if len(y) > 0 :
                if y[0] not in list_cve:
                    list_cve.append(y[0])
                    print (y[0])
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ########################################################################################

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Ports found (**)\n")

        imp_ports = open('scan_ports.txt','r')

        regex = '[0-9]+/[\w.]+\s*[\w.]+\s*[\w.]+.[\w.]+'

        list_port = []

        for line2 in imp_ports:
            line2 = line2.rstrip()
            x = re.findall('[0-9]+/[\w.]+\s*[\w.]+\s*[\w.]+.[\w.]+', line2)
            if len(x) > 0 :
                if x[0] not in list_port:
                    list_port.append(x[0])
                    print (x[0])
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")


        #########################################################################################

        ########################################################################################

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Query pages (**)\n")

        imp_page = open('scan_page.txt','r')

        regex2 = '[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+'

        list_pages = []

        for line3 in imp_page:
            line3 = line3.rstrip()
            z = re.findall('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+[A-Za-z]+', line3)

            if len(z) > 0 :
                if z[0] not in list_pages:
                    list_pages.append(z[0])
                    print (z[0])
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")


        #########################################################################################

        ########################################################################################

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" The website is vulnerable to (**)\n")

        imp_vulnerab = open('scan_page.txt','r')

        #regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_vulnerab = []

        for line4 in imp_vulnerab:
            line4 = line4.rstrip()
            a = re.findall('-\s[A-Z].*', line4)
            if len(a) > 0 :
                if a[0] not in list_vulnerab:
                    list_vulnerab.append(a[0])
                    print (a[0])

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
 

        ###############################################################################################

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Mailings found (**)\n")
        mail_search = open('scan_mails.txt','r')
        
        #[\w.]+.[0-9]+.[\w.]+.\n
        #regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_mail = []

        for line5 in mail_search:
            line5 = line5.rstrip()
            a = re.findall('[\w+]+@[\w+]+.[\w+]+.[\w+]+', line5)
            if len(a) > 0 :
                if a[0] not in list_mail:
                    list_mail.append(a[0])
                    print (a[0])

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")


        ###############################################################################################

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" CMS (**)\n")

        vers_search = open('scan_page.txt','r')
        #[\w.]+.[0-9]+.[\w.]+.\n
        #regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_vers = []

        for line6 in vers_search:
            line6 = line6.rstrip()
            p = re.findall('.[+].\s[\w.]+\s[\w]+\s[0-9]+.[0-9]+.[0-9]', line6)
            if len(p) > 0 :
                if p[0] not in list_vers:
                    list_vers.append(p[0])
                    #print (p[0])
                    init()
                    print (Fore.WHITE + (p[0]))

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")


        ###############################################################################################

        
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Address (**)\n")

        ip_s = open('scan_version.txt','r')
        #[\w.]+.[0-9]+.[\w.]+.\n
        #regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        #:\s[0-9]+.[0-9]+.[0-9]+.[0-9]+\s
        ip_d = []

        for line7 in ip_s:
            line7 = line7.rstrip()
            q = re.findall('[IP]+..........[0-9]+.[0-9]+.[0-9]+.[0-9]+.', line7)
            if len(q) > 0 :
                if q[0] not in ip_d:
                    ip_d.append(q[0])
                    #print (p[0])
                    init()
                    print (Fore.WHITE + (q[0]))

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")


        ###############################################################################################

        
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Location (**)\n")

        location_g = open('scan_version.txt','r')
        #[\w.]+.[0-9]+.[\w.]+.\n
        #regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        #:\s[0-9]+.[0-9]+.[0-9]+.[0-9]+\s
        local_d = []

        for line8 in location_g:
            line8 = line8.rstrip()
            f = re.findall('[\w]+\s\s\s.\s[A-Z]+\s[A-Z]+', line8)
            if len(f) > 0 :
                if f[0] not in local_d:
                    local_d.append(f[0])
                    #print (p[0])
                    init()
                    print (Fore.WHITE + (f[0]))

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
    elif opcion == 5:
        print ("")
        init()  
        print(Fore.RED + "[*]"+Fore.WHITE+"    Hello and welcome to " +Fore.GREEN+ "F-Scan (**)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   With this script you can optimize your time, reducing the time you audit a page ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   web since T.rex_scan executes the task you indicate and filters the results.  ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   the idea was born whenWe had to audit a web page and we had to open many consoles")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   to run toolper tool, in addition to this we had to analyze the logs one by one and ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   take out the informationthat we needed, T.rex_scan is a Swiss Army knife has several ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   tools for daily use and filtersthe results.\n")
        init()
        print(Fore.GREEN + "[!]"+Fore.WHITE+"  Show the vulnerabilities of the audited page")
        init()
        print(Fore.GREEN + "[!]"+Fore.WHITE+"  Launch a port scan")
        init()
        print(Fore.GREEN + "[!]"+Fore.WHITE+"  Show the CVEs associated with the page")
        init()
        print(Fore.GREEN + "[!]"+Fore.WHITE+"  Search for emails associated with the domain")
        init()
        print(Fore.GREEN + "[!]"+Fore.WHITE+"  It shows the IP address and the hosting server location\n")
        init()
        print(Fore.RED + "[!]"+Fore.WHITE+"  This script makes use of and depends on the following tools for its operation " +Fore.GREEN+ ":\n")
        init()
        print(Fore.CYAN + "[1]"+Fore.WHITE+"       WPScan V 2.9.3")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"       Nmap V 7.60")
        init()
        print(Fore.CYAN + "[3]"+Fore.WHITE+"       Theharvester V 2.7")
        init()
        print(Fore.CYAN + "[4]"+Fore.WHITE+"       WhatWeb V 0.4.9\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   In the same way, T.rex_scan makes use of regular expressions to filter the ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   data that we need,use of the libraries (os, time, re, time, color, tqdm and sleep)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   It is important to keep in mind that if you are going to use Kali linux you  ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   should only install the tqdm librarybut if you are going to use Windows you")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   must install all the libraries with the option pip install \n\n")
        


    elif opcion == 6:
        salir = True
    else:
        print ("Enter a number between 1 and 5")
print ("") 
print ("********Finished script***********")
print ("")

#comandos error

"""ping 
 apt-cache show nmap
 apt-cache search nmap
 sudo apt-get install python-nmap
 sudo apt-get install python3-nmap
"""


