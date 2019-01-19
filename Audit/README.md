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

