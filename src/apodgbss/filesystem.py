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
import os
import re
import sys

import ccalogging

from apodgbss import errorExit, errorNotify, errorRaise

log = ccalogging.log


def fileNameFromString(xstr):
    """Convert a string to a valid filename, capitalising the first letter of each word."""
    try:
        remove = "!\\/:*?\"<>|@#$%^&()+={}[].;'`,~_-"
        for char in remove:
            xstr = xstr.replace(char, "")
        xstr = xstr.replace("https", "")
        xstr = xstr.replace("http", "")
        tmp = xstr.split(" ")
        op = ""
        for word in tmp:
            if word != "":
                op = f"{op}{word[0].upper()}{word[1:]}"
        return op
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def cleanFileName(xstr):
    """Convert a string to a valid filename stub, removing invalid characters."""
    try:
        return re.sub(r"[^a-zA-Z0-9]", "", xstr)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def writeLines(fn, lines):
    try:
        with open(fn, "w") as f:
            for line in lines[:-1]:
                f.write(line + "\n")
            f.write(lines[-1])
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def findProperDirectory(directory):
    try:
        if os.path.isdir(directory):
            return directory
        xdir = os.path.abspath(directory)
        if os.path.isdir(xdir):
            return xdir
        xdir = os.path.abspath(os.path.expanduser(directory))
        if os.path.isdir(xdir):
            return xdir
        xdir = Path.home() / directory
        if xdir.is_dir():
            return xdir
        xdir = Path.home() / "Pictures" / directory
        if xdir.is_dir():
            return xdir
        raise Exception(f"Directory {directory} not found.")
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def filterDir(directory, filter=[".jpg", ".png", ".jpeg"]):
    try:
        if not os.path.isdir(directory):
            raise Exception(f"filterDirectory: Directory {directory} not found.")
        files = os.listdir(directory)
        return [
            f
            for f in files
            if os.path.splitext(f)[1].lower() in filter
            and os.path.isfile(os.path.join(directory, f))
        ]
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)
