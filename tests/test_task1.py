# tests cases for the task1

from unittest import mock

import app


def test_requests_import():
    assert "requests" in dir(app), "You are yet to import the requests module, use 'import requests' to import it"

