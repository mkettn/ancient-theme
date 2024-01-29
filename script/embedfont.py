#!/usr/bin/env python3
# Copyright (c) 2024 Mark Kettner
# SPDX-License-Identifier: MIT
"""
embed fonts b64 encoded into stylesheets.

Usage:
  ./embedfont.py [options] <file>

options:
  -o FILE  output file.

"""
from docopt import docopt
from base64 import b64encode
import mimetypes
from sys import stdout
from os.path import basename, splitext

ARGS = docopt(__doc__)
mimetypes.init()

def embedfont(ifp, ofd):
    name, _ = splitext(basename(ifp))
    mtype, _ = mimetypes.guess_type(ifp)
    print(f"@font-face{{font-family:'{name}';font-style:normal;src:url(data:{mtype};base64,",
          file=ofd, end='')
    with open(ifp, "rb") as fd:
        print(b64encode(fd.read()).decode().strip(), file=ofd, end='')
    print(");}}", file=ofd)

if ARGS["-o"]:
    with open(ARGS["-o"], 'w') as ofd:
        embedfont(ARGS["<file>"], ofd)
else:
    embedfont(ARGS["<file>"], stdout)
