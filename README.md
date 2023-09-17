# NASA APOD Gnome Background Slideshow

NASA Astronomy Picture of the Day (APOD) Grabber and Gnome Background Slide show Setter

## Dependencies

* [requests](https://requests.readthedocs.io/en/latest/)
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)

## What this does

`apodgbss` will read the archive page for APOD and randomly pick 10 pictures.

It then downloads those 10 pictures into your Pictures folder in a sub-directory
called `apod`.

It will then generate the xml format files required by gnome to show them as a
slideshow for the desktop background.

All data is cached to not overstress the APOD servers, therefore should a
picture be chosen more than once there is no need to re-download it.
