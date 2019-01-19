#!/bin/bash

set -e
cd "$1"
git init
git config --local user.name 'git_autocommit'
git config --local user.email 'git@localhost'
