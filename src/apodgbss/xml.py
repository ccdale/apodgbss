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
import sys
import xml.etree.ElementTree as ET

import ccalogging

from apodgbss import __appname__, errorExit, errorNotify, errorRaise

log = ccalogging.log


def makeGnomePropsXML(xname, fqfn):
    try:
        lines = ["<?xml version='1.0' encoding='UTF-8'?>"]
        lines.append("<!DOCTYPE wallpapers SYSTEM 'gnome-wp-list.dtd'>")
        wallpapers = ET.Element("wallpapers")
        wallpaper = ET.SubElement(wallpapers, "wallpaper", deleted="false")
        name = ET.SubElement(wallpaper, "name")
        name.text = xname
        filename = ET.SubElement(wallpaper, "filename")
        filename.text = fqfn
        options = ET.SubElement(wallpaper, "options")
        options.text = "zoom"
        tree = ET.ElementTree(wallpapers)
        ET.indent(tree, "  ")
        xstr = ET.tostring(
            wallpapers, encoding="unicode", method="xml", short_empty_elements=False
        )
        tmp = xstr.split("\n")
        lines.extend(tmp)
        return lines
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def makeStatic(root, fname, duration=60):
    try:
        static = ET.SubElement(root, "static")
        dur = ET.SubElement(static, "duration")
        dur.text = str(duration)
        file = ET.SubElement(static, "file")
        file.text = fname
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def makeTransition(root, fromfile, tofile, transduration=2):
    try:
        transition = ET.SubElement(root, "transition")
        dur = ET.SubElement(transition, "duration")
        dur.text = str(transduration)
        xfrom = ET.SubElement(transition, "from")
        xfrom.text = fromfile
        xto = ET.SubElement(transition, "to")
        xto.text = tofile
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def makeSlideShowXML(fqfns, duration=60, transduration=2, xname=__appname__):
    try:
        cnfiles = len(fqfns)
        log.info(f"new slideshow with {cnfiles} picture files for {xname}")
        background = ET.Element("background")
        for cn, fqfn in enumerate(fqfns):
            makeStatic(background, fqfn, duration)
            if cn + 1 < cnfiles:
                fnnext = fqfns[cn + 1]
                makeTransition(background, fqfn, fnnext, transduration)
            else:
                makeTransition(background, fqfn, fqfns[0])
        lines = ["<?xml version='1.0' encoding='UTF-8'?>"]
        tree = ET.ElementTree(background)
        ET.indent(tree, "  ")
        xstr = ET.tostring(
            background, encoding="unicode", method="xml", short_empty_elements=False
        )
        tmp = xstr.split("\n")
        lines.extend(tmp)
        return lines
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
