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
