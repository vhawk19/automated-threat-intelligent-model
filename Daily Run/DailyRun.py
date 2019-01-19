#"Helper" program for main BROFormatter.py, this script is run daily by a cronjob

#Necessary Imports
import BROFormatter
import time
import os
from datetime import datetime


start_time = time.clock() #To calculate total time taken

today = datetime.today().strftime('%Y-%m-%d') #To create daily pull folder


try:
    sources = open('sources.txt', 'r')  #Note: this contains direct links to the intel files from each source
except FileNotFoundError:
    print("sources.txt does not exist")
    sys.exit()

try:
    log_path = sources.readline().replace('\\', '/')  #Logs folder path is pulled from the first line of 'sources.txt'
    log_path = log_path.replace('\n', '')
except:
    print("Log folder path is not valid")
    sys.exit()

if not os.path.exists(log_path):  #Creates initial Logs folder if software has just been installed
    os.makedirs(log_path)

newpath = log_path + "/WCIQ-" + today  #Creates daily pull folder
if not os.path.exists(newpath):
    os.makedirs(newpath)


log = open(newpath + '/log.txt','w')  #Only the main log file is created here, all other logs are created in main program


log.write("Start Time: "+ str(datetime.now()) + '\n')

counter = BROFormatter.bro_generator(newpath)  #Runs main program, collects number of intel items analyzed

log.write("End Time: "+ str(datetime.now()) + '\n')
log.write("Total time taken: " + str(time.clock() - start_time) + " seconds\n")
log.write("Total intel items processed: "+ str(counter) + '\n')
log.close()

#input()
