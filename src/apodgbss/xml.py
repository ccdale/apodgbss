import os
import sys
import xml.etree.ElementTree as ET

import ccalogging

from apodgbss import __appname__, errorExit, errorNotify, errorRaise
from gwss.files import filesAndName

log = ccalogging.log


def makeGnomePropsXML(xname):
    try:
        lines = ["<?xml version='1.0' encoding='UTF-8'?>"]
        lines.append("<!DOCTYPE wallpapers SYSTEM 'gnome-wp-list.dtd'>")
        wallpapers = ET.Element("wallpapers")
        wallpaper = ET.SubElement(wallpapers, "wallpaper", deleted="false")
        name = ET.SubElement(wallpaper, "name")
        name.text = xname
        filename = ET.SubElement(wallpaper, "filename")
        filename.text = os.path.join(gwss.xmloutputdir, f"{xname}.xml")
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


def makeStatic(root, fname):
    try:
        static = ET.SubElement(root, "static")
        dur = ET.SubElement(static, "duration")
        dur.text = str(gwss.duration)
        file = ET.SubElement(static, "file")
        file.text = fname
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def makeTransition(root, fromfile, tofile):
    try:
        transition = ET.SubElement(root, "transition")
        dur = ET.SubElement(transition, "duration")
        dur.text = str(gwss.transduration)
        xfrom = ET.SubElement(transition, "from")
        xfrom.text = fromfile
        xto = ET.SubElement(transition, "to")
        xto.text = tofile
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def makeSlideShowXML(fqfns):
    try:
        cnfiles = len(fqfns)
        log.info(f"new slideshow with {cnfiles} picture files for {__appname__}")
        background = ET.Element("background")
        for cn, fqfn in enumerate(fqfns):
            makeStatic(background, fqfn)
            if cn + 1 < cnfiles:
                fnnext = fqfns[cn + 1]
                makeTransition(background, fqfn, fnnext)
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
