Harvest
=======

Harvest gathers Threat Intelligence Feeds from publicly available sources

You can run the tool with `python combine.py`:
```
usage: combine.py [-h] [-t TYPE] [-f FILE] [-d] [-e] [--tiq-test]

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Specify output type. Currently supported: CSV and exporting to CRITs
  -f FILE, --file FILE  Specify output file. Defaults to harvest.FILETYPE
  -d, --delete          Delete intermediate files
  -e, --enrich          Enrich data
  --tiq-test            Output in tiq-test format (implies -e)
```

Alternately, you can run each phase individually:


````
python reaper.py
python thresher.py
python winnower.py
python baler.py
````

The output will actually be a CSV with the following schema:
```
entity, type, direction, source, notes, date
```

Output Screenshot:
<img src="https://66.media.tumblr.com/70f79f7b276637864af713d5e4b16e31/tumblr_plkxbbMoxE1wnca1uo1_1280.png" alt="Harvested Output">
<img src="https://66.media.tumblr.com/83ac842be4ad11b73a6bde8d349f4699/tumblr_plkxg0oSXy1wnca1uo1_540.png" alt="Harvested Output">

### Installation

Installation for *NIX systems.

```
sudo apt-get install python-dev python-pip python-virtualenv git
git clone https://github.com/kaiiyer/automated-threat-intelligent-model.git
cd combine
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

At this point you should be ready to go.

