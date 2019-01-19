#!/usr/bin/env python2

import os
import sys
import datetime

import mss


filename = os.path.join(sys.argv[1],datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".png")

with mss.mss() as sct:
    sct.shot(mon=-1, output=filename)

