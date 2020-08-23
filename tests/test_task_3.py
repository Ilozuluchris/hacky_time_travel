""""
tests cases for the task 3
"""

from unittest import mock

import pytest

import app


def test_beautifulsoup_import():
    assert "BeautifulSoup" in dir(app), "You have not imported beautifulsoup, please import with `from bs4 import BeautifulSoup`"


def test_get_events_exists():
    assert "get_events" in dir(app), "Create the get_events function"

# def test_get_events_soup():
#     c = app.get_events
#     print(c.__dict__)
#     print('//......')
#     print(c.__code__)
#     assert isinstance(c.__annotations__, int)
