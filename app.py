from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


def getData():
    website_url = "https://www.onthisday.com/"
    try:
        res = requests.get(website_url)
    except RequestException:
        return {'status': False}
    return {'status': True, "content": res.text}
