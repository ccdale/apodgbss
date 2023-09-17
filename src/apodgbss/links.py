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

from bs4 import BeautifulSoup as bs
import ccalogging

from apodgbss import __version__, __appname__, errorExit, errorNotify, errorRaise
from apodgbss.cache import cacheUrl, cachePicture


def getArchivePageLinks(rooturl):
    try:
        url = "/".join([rooturl, "archivepix.html"])
        data = cacheUrl(url)
        bspage = bs(data, "html.parser")
        root = os.path.dirname(url)
        links = ["/".join([root, link.get("href")]) for link in bspage.find_all("a")]
        r = re.compile(r".*/ap[0-9]+\.html$")
        xlinks = list(filter(r.match, links))
        return xlinks
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getImageFromLink(link):
    try:
        r = getUrl(link)
        bspage = bs(r.text, "html.parser")
        img = bspage.find("img")
        pass
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
