from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


def get_data():
    website_url = "https://www.onthisday.com/"
    try:
        res = requests.get(website_url)
    except RequestException:
        return {'status': False}
    return {'status': True, "content": res.text}


def get_events(data):
    X = 6


if __name__=="__main__":
    print(get_data())
