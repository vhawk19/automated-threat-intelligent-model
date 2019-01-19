#!/bin/bash

if [ -f $(which apt) ];
then
	echo -e "\x1b[32m[Installing git and pip]\x1B[0m"
	sudo apt-get -yq update && sudo apt-get install -yq git python python-pip
fi

echo -e "\x1b[32m[Installing python requirements]\x1B[0m"
pip install --user -r requirements.txt

echo -e "\x1b[32m[Installing in /usr/local/bin]\x1B[0m"
sudo mkdir /usr/local/bin/_audit.py
sudo cp -r . /usr/local/bin/_audit.py/
sudo ln -sf /usr/local/bin/_audit.py/audit.py /usr/local/bin/audit.py

echo -e "\x1b[32m[DONE]\x1B[0m"

exec $SHELL
