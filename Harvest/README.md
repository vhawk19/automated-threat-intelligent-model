Harvest
=======

Harvest gathers Threat Intelligence Feeds from publicly available sources

You can run the core tool with `combine.py`:
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
- The `entity` field consists of a FQDN or IPv4 address (supported entities at the moment)
- The `type` field consists of either `FQDN` or `IPv4`, classifying the type of the entity
- The `direction` field will be either `inbound` or `outbound`
- The `source` field contains the original URL.
- The `notes` field should cover any extra tag info we may want to persist with the data
- The `date` field will be in `YYYY-MM-DD` format.
- All fields are quoted with double-quotes (`"`).

Output Screenshot:
<img src="https://66.media.tumblr.com/70f79f7b276637864af713d5e4b16e31/tumblr_plkxbbMoxE1wnca1uo1_1280.png" alt="Harvested Output">

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

