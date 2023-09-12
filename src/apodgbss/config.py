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

import configparser
import os
from pathlib import Path
import sys

import ccalogging

from apodgbss import __version__, __appname__, errorExit, errorNotify, errorRaise

"""config module for apodgbss"""

log = ccalogging.log


class ConfigFileNotFound(Exception):
    pass


def cfgFn(overrideappname=None):
    try:
        cfgfilename = overrideappname if overrideappname else __appname__
        return Path.home() / ".config" / f"{cfgfilename}.cfg"
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def askConfig(overrideappname=None):
    """ask the user for configuration information"""
    try:
        print()
        print(f"Welcome to {__appname__} {__version__}")
        print()
        print(
            "Pick a mirror site from the list at: https://apod.nasa.gov/apod/lib/about_apod.html"
        )
        mirrorsiteurl = input("Mirror site URL: ")
        config = configparser.ConfigParser()
        config["NASA"] = {"mirrorsiteurl": mirrorsiteurl}
        return config
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


def writeConfig(cfg, overrideappname=None):
    try:
        cfgfn = cfgFn(overrideappname)
        with open(cfgfn, "w") as cfgfile:
            cfg.write(cfgfile)
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def readConfig(overrideappname=None):
    try:
        cfgfn = cfgFn(overrideappname)
        if not cfgfn.exists():
            config = askConfig(overrideappname)
            writeConfig(config, overrideappname)
        elif not cfgfn.exists():
            raise ConfigFileNotFound(f"Config file {cfgfn} not found")
        else:
            config = configparser.ConfigParser()
            config.read(cfgfn)
        return config
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)
