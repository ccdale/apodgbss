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

from apodgbss import __appname__
from apodgbss.config import cfgFn, readConfig, writeConfig


def test_cfgFn():
    assert str(cfgFn()) == os.path.expanduser(f"~/.config/{__appname__}.cfg")


def test_cfgFn_overrideappname():
    assert str(cfgFn("test")) == os.path.expanduser(f"~/.config/test.cfg")


def test_writeConfig():
    config = configparser.ConfigParser()
    config["NASA"] = {"mirrorsiteurl": "https://apod.nasa.gov/apod/"}
    assert writeConfig(config, overrideappname="test") == None
    fqfn = cfgFn("test")
    assert os.path.exists(fqfn)
    os.remove(fqfn)
    assert not os.path.exists(fqfn)


def test_readConfig():
    config = configparser.ConfigParser()
    sect = "NASA"
    key = "mirrorsiteurl"
    value = "https://apod.nasa.gov/apod/"
    config[sect] = {key: value}
    writeConfig(config, overrideappname="test")
    assert os.path.exists(cfgFn("test"))
    xconfig = readConfig(overrideappname="test")
    assert xconfig[sect][key] == value
    os.remove(cfgFn("test"))
