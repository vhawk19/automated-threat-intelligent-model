#!/bin/bash

set -e
cd "$1"
git add .
git commit -m "`date`"
