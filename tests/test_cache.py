from apodgbss.cache import cacheUrl


def test_cacheUrl():
    url = "https://apod.nasa.gov/apod/image/2101/OrionDeep_WISErizzo_960.jpg"
    ufn = cacheUrl(url)
    assert (
        str(ufn)
        == "/home/chris/.cache/apodgbss/httpsapodnasagovapodimage2101OrionDeepWISErizzo960jpg"
    )
