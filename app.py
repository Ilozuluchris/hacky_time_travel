import requests

def getData():
    website_url = "https://www.onthisday.com/"
    res = requests.get(website_url)
    if res.status_code == 200:
        return {'status': True, "data": res.text}
    else:
        return {'status': False}
