After setting up, you can dive in

# 1 Setup
## Setup
- Create a virtual environment
    - Using pipenv: pipenv shell --python 3, install pipenv via `pip install pipenv`
-   Install requirements
    - Using pipenv: pipenv install -r requirements.txt
-  Verify setup run pytest, all the tests should fail, which is a good thing.

## Viewing your work
- Use flask run to view your work

# 2 Getting site data
In order to scrape for data we need to first download the html page of the site, we use the requests library for this
- Import requests into app.py using `import requests` and `from requests.exceptions import RequestException` which would be used to handle errors
- Define a function called getData.
  - create a variable to hold the site url `site_url="https://www.onthisday.com/"`
  - download the page data using requests `res = requests.get(website_url)`
  -  Catch the RequestException
   using a try catch.
  - If the exception is thrown return a dictionary with only key 'status' that maps to false
  - If the exception doesnot occur, return a dictionary with two keys:
    - The 'status' key maps to `True`
    - The 'content' key maps to `res.text`


# 3 Getting a list of events(Parsing site data)
We can get the list of events by parsing through the html contents we got from the previous step
- First off create a function called getEvents, this function would be receiving only one argument which is the dictionary gotten from the getData fxn
- Check the argument passed in, has its status check as true using an if statement
- If the check passes, pass "data['result']" into the `BeautifulSoup()` constructor and save it to a variable ie soup = BeautifulSoup(site_html)
- Next we get the HTML elements that contain the actual events. To do we use the css selector of those elements which is  ".event-list--with-advert>.event"(to find this you inspect the html of the page via the browser), the pass this
css selector into the "select method"  of the soup(the variable created in the previous soup) ie:soup.select(".event-list--with-advert>.event").
- Return the variable  gotten from the last step as the only result of  the function //test the returned type


# 4 Reformatting event list data
While we have succeffully scraped for events data, we need to present it in a more friendly manner.
- First create, a function called
