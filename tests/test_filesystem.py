from apodgbss.filesystem import cleanFileName, fileNameFromString


def test_fileNameFromString():
    xstr = "This is a test string"
    fname = fileNameFromString(xstr)
    assert fname == "ThisIsATestString"


def test_fileNameFromString_extra():
    xstr = "This is a test string with extra characters 1234567890!@#$%^&*()_+{}[]|\\:;\"'<>?,./`~"
    fname = fileNameFromString(xstr)
    assert fname == "ThisIsATestStringWithExtraCharacters1234567890"


def test_cleanFileName():
    xstr = "This is a test string"
    fname = cleanFileName(xstr)
    assert fname == "Thisisateststring"


def test_cleanFileName_extra():
    xstr = "This is a test string with extra characters 1234567890!@#$%^&*()_+{}[]|\\:;\"'<>?,./`~"
    fname = cleanFileName(xstr)
    assert fname == "Thisisateststringwithextracharacters1234567890"
