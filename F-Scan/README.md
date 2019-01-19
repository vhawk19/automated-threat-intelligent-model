# F-Scan
Script in its version 0.2, T.rex_scan only facilitates the visualization when auditing a web page, its next versions will allow the researcher to make attacks and generate reports with just one click


With this script you can optimize your time, reducing the time you audit a page web since T.rex_scan executes the task you indicate and filters the results. the idea was born when We had to audit a web page and we had to open many consoles to run tool per tool, in addition to this we had to analyze the logs one by one and take out the information that we needed, T.rex_scan is a Swiss Army knife has several tools for daily use and filters the results.

<h2>Final version </h2>

It is expected that this script in its next versions will analyze a web page and if this is vulnerable the attack to get access to your passwords and information, will finally deliver a report with what was found in the analysis.

<h2>Improvements that will be implemented:</h2>
 
* Shows vulnerabilities of the audited page
* Launch a port scan
* Shows the CVEs associated with the vulnerabilities of the page
* Search for emails associated with the domain
* Shows the IP address and hosting server location

This script makes use of and depends on the following tools for its operation:

* WPScan V 2.9.3
* Nmap V 7.60
* Theharvester V 2.7
* WhatWeb V 0.4.9
* Colorama
* tqdm


This script makes use of regular expressions to filter the data that we need, use of the libraries (os, time, re, time, color, tqdm and sleep)

It is important to keep in mind that if you are going to use Kali linux you should only install the tqdm library but if you are going to use Windows you must install all the libraries with the option pip install

Installation / use

* git clone https://github.com/davenisc/T.rex_scan/tree/0.2
* cd T.rex_scan
* pip install -r requirements.txt
* python T.rex_scan.py
* option 5 for more details of F-Scan


