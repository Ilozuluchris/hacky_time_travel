""""
tests cases for the task 3
"""

from unittest import mock

import pytest

import app


def test_beautifulsoup_import():
    assert "BeautifulSoup" in dir(app), "You have not imported beautifulsoup, please import with `from bs4 import BeautifulSoup`"


def test_getEvents_exists():
    assert "getEvents" in dir(app), "Create the getEvents function"

# def test_getEvents_soup():
#     c = app.getEvents
#     print(c.__dict__)
#     print('//......')
#     print(c.__code__)
#     assert isinstance(c.__annotations__, int)
