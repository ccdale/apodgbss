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

from apodgbss import __version__, errorExit
from apodgbss.filesystem import filterDir, findProperDirectory, writeLines
from apodgbss.xml import makeGnomePropsXML, makeSlideShowXML

"""This is the slideshow from directory module."""

# ccalogging.setDebug()
ccalogging.setInfo()
ccalogging.setConsoleOut()
log = ccalogging.log


def doDir():
    try:
        log.info(f"Starting doDir {__version__}...")
        if len(sys.argv) < 2:
            raise Exception("No directory specified.")
        xdir = findProperDirectory(sys.argv[1])
        xname = os.path.basename(xdir)
        pics = filterDir(xdir)
        localpath = Path.home() / ".local" / "share"
        ssdir = "/".join([str(localpath), "gnome-wallpaper-slideshows"])
        propdir = "/".join([str(localpath), "gnome-background-properties"])
        ssfn = "/".join([ssdir, f"{xname}.xml"])
        propfn = "/".join([propdir, f"{xname}.xml"])
        sslines = makeSlideShowXML(pics, xname=xname)
        writeLines(ssfn, sslines)
        log.info(f"Slide show XML written to {ssfn}.")
        proplines = makeGnomePropsXML("APOD", ssfn)
        writeLines(propfn, proplines)
        log.info(f"Properties XML written to {propfn}.")
        log.info(f"doDir {__version__} completed.")
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
