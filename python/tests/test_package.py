import pytest

import pylinguis

def test_banner():
    assert pylinguis.banner().startswith("Linguis")

def test_version():
    vMajor, vMinor = pylinguis.version()
    assert vMajor != None
    assert vMinor != None
