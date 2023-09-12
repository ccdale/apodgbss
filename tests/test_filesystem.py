from apodgbss.filesystem import fileNameFromString


def test_fileNameFromString():
    xstr = "This is a test string"
    fname = fileNameFromString(xstr)
    assert fname == "ThisIsATestString"


def test_fileNameFromString_extra():
    xstr = "This is a test string with extra characters 1234567890!@#$%^&*()_+{}[]|\\:;\"'<>?,./`~"
    fname = fileNameFromString(xstr)
    assert fname == "ThisIsATestStringWithExtraCharacters1234567890"
