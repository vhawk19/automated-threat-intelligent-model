#!/usr/bin/env python2

import sys
import re
import os

from ansi2html import Ansi2HTMLConverter


def removebells(text):
    return text.replace('\07', '')


def removebackspaces(text):
    backspace_or_eol = r'(.\010)|(\033\[K)'
    n = 1
    while n > 0:
        text, n = re.subn(backspace_or_eol, '', text, 1)
    return text


def script_to_html(filename, output_filename):
	conv = Ansi2HTMLConverter(dark_bg=True, font_size=18)
	with open(filename, 'r') as f:
		ansi = f.read()
	ansi = ansi.decode('utf-8', errors='ignore')
	ansi = removebells(ansi)
	ansi = removebackspaces(ansi)
	html = conv.convert(ansi)

	with open(output_filename, 'w') as f:
		f.write(html.encode('utf8'))


if __name__ == "__main__":

	if len(sys.argv) < 3:
		print "Usage: %s <ansi_file> <output_file>" % sys.argv[0]
		exit(1)

	if os.path.exists(sys.argv[1]):
		script_to_html(sys.argv[1], sys.argv[2])
		print "OK"
	else:
		print "File does not exist"
