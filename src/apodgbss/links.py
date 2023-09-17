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

log = ccalogging.log


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


def getImageFromLink(rooturl, linkurl):
    try:
        data = cacheUrl(linkurl)
        bspage = bs(data, "html.parser")
        img = bspage.find("img")
        if img is not None:
            imgurl = img.get("src")
            pfn = cachePicture("/".join([rooturl, imgurl]))
            log.info(f"image cached at {pfn}")
            return pfn
        else:
            log.info(f"no image found at {linkurl}")
            return None
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
