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

import random
import sys

import ccalogging

from apodgbss import __version__, __appname__, errorExit, errorNotify, errorRaise
from apodgbss.config import readConfig, writeConfig
from apodgbss.links import getArchivePageLinks, getImageFromLink

"""This is the NASA Astronomical Picture of the Day (APOD) Gnome Background Setter (GBSS) module."""

ccalogging.setDebug()
# ccalogging.setInfo()
ccalogging.setConsoleOut()
log = ccalogging.log


def goBabe():
    """The entry point for the apodbbss module."""
    try:
        log.info(f"Starting {__appname__} {__version__}...")
        cfg = readConfig()
        rooturl = "/".join([cfg["NASA"]["mirrorsiteurl"], "apod"])
        links = getArchivePageLinks(rooturl)
        chosen = random.choice(links, k=10)
        print(chosen)
        # TODO: Add code here.
        writeConfig(cfg)
        log.info(f"{__appname__} {__version__} completed.")
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
