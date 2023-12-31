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

from pathlib import Path
import random
import sys

import ccalogging

from apodgbss import __version__, __appname__, errorExit, errorNotify, errorRaise
from apodgbss.config import readConfig, writeConfig
from apodgbss.filesystem import writeLines
from apodgbss.links import getArchivePageLinks, getImageFromLink
from apodgbss.xml import makeGnomePropsXML, makeSlideShowXML

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
        chosen = random.choices(links, k=10)
        pictures = []
        for c in chosen:
            pfn = getImageFromLink(rooturl, c)
            if pfn is not None:
                pictures.append(pfn)
        localpath = Path.home() / ".local" / "share"
        ssdir = "/".join([str(localpath), "gnome-wallpaper-slideshows"])
        propdir = "/".join([str(localpath), "gnome-background-properties"])
        ssfn = "/".join([ssdir, "apod.xml"])
        propfn = "/".join([propdir, "apod.xml"])
        sslines = makeSlideShowXML(pictures)
        writeLines(ssfn, sslines)
        log.info(f"Slide show XML written to {ssfn}.")
        proplines = makeGnomePropsXML("APOD", ssfn)
        writeLines(propfn, proplines)
        log.info(f"Properties XML written to {propfn}.")
        writeConfig(cfg)
        log.info(f"{__appname__} {__version__} completed.")
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
