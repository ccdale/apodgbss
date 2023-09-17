#
# Copyright (c) 2023, Chris Allison
#
#     This file is part of apodgbss.
#
#     apodgbss is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     apodgbss is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with apodgbss.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from pathlib import Path
import sys

import ccalogging

from apodgbss import __appname__, errorExit, errorNotify, errorRaise
from apodgbss.filesystem import cleanFileName
from apodgbss.internet import getUrl

"""cache module for apodgbss."""

log = ccalogging.log


def cacheUrl(url):
    try:
        cachedir = Path.home() / ".cache" / __appname__
        if not cachedir.exists():
            log.info(f"Creating cache directory {cachedir}")
            cachedir.mkdir(parents=True)
        ufn = cachedir / cleanFileName(url)
        if not ufn.exists():
            log.info(f"Downloading {url} to {ufn}")
            r = getUrl(url)
            ufn.write_text(r.text)
            data = r.text
        else:
            log.info(f"URL {url} already cached at {ufn}")
            with open(ufn, "r") as f:
                data = f.read()
        return data
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def cachePicture(url):
    try:
        picdir = Path.home() / "Pictures" / __appname__
        if not picdir.exists():
            log.info(f"Creating picture cache directory {picdir}")
            picdir.mkdir(parents=True)
        pfn = picdir / os.path.basename(url)
        if not pfn.exists():
            log.info(f"Downloading Picture {url} to {pfn}")
            r = getUrl(url)
            pfn.write_bytes(r.content)
        else:
            log.info(f"Picture {url} already cached at {pfn}")
        return str(pfn)
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)
