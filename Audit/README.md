# audit.py

Simple tool designed to help keeping tracks of security audits / engagements. Logs activity to a dedicated folder for each audit.

It currently supports:
- shell output logging
- periodic screenshots
- automated git versioning of the audit folder

## Setup

Quick install:

```
./install.sh
```

Dependencies:

* python2
* git
* mss (pip)
* termcolor (pip)
* ansi2html (pip)

## Usage

Edit **config.py** to suit your needs.
```
$ audit.py config
```

Create audit project:
```
$ audit.py init audit1
```

Start/Resume logging:
```
$ audit.py start audit1 
```

Stop/Pause logging:
```
$ audit.py stop audit1
```

Export shell log to HTML:
```
$ audit.py export audit1
```

All audit logs are saved in the main audit folder defined in **config.py**, in a subdirectory "audit1".

## Output
Screenshot Captured during the Audit
<img src="https://66.media.tumblr.com/bace382b9f00fab7de7840fd271b82bb/tumblr_plkyem0UUI1wnca1uo1_1280.png" alt="Harvested Output">
    

