## Setup

Run Terminal Command:
```
sudo crontab -e
```
Add text:
```
00 02 * * * python path/to/software/folder/DailyRun.py

(Change 00 02 to preferred daily run time)
```

## Revisions:

Add new sources to "sources.txt" in proper format
Note: URL needs to lead directly to intel file

To change location of "Logs" directory, replace first line of "sources.txt" with new file path

## Data Interpretation:

Daily pull is stored in new WCIQ-Year-Month-Date folder in /Logs 
-formatted-intel.txt contains processed output
-log.txt contains start and end times, total time taken, number of processed items
-errors-log.txt contains descriptions of any errors encountered during run
-repeats-log.txt contains list of repeated intel (all types of intel)

## Screenshot of logs
<img src="https://66.media.tumblr.com/13e9355fa87ca66c96bbaccbe31276e7/tumblr_plldonr0CD1wnca1uo1_1280.png" alt="Sceenshot">
