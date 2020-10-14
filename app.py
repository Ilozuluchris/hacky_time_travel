"""
This is where you would write your code
"""
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


def get_events(site_data):
    if site_data['status']:
        site_html = site_data['content']

        soup = BeautifulSoup(site_html, "html.parser")
        events_list = soup.select(".event-list--with-advert>.event")
        return events_list
    return None


def format_events(events):
    formatted_events = []
    if events is not None:
        for event in events:
            event_year, event_details = event.text.split(" ", 1)
            d = dict(year=event_year, details=event_details)
            formatted_events.append(d)
    return formatted_events



if __name__=="__main__":
    print(get_data())
