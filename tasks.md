After setting up, you can dive in

# 1 Setup
## Setup
- Create a virtual environment, personally I use pipenv, but use the method you are most comfortable with.
    - Using pipenv: Install pipenv if you have not via `pip install pipenv`and create the environment via `pipenv shell --python 3`;
-   Install requirements
    - Using pipenv: `pipenv install -r requirements.txt
-  Verify setup run `ptw` or `pytest-watch`, all the tests should fail, which is a good thing. As you go through this project all the tests would pass!

## Viewing your work, move to intro
- Use flask run to view your work; todo might need to specify export, pass debug explicilty to the flask app

# 2 Getting site data
We would be using `https://www.onthisday.com/` to get the events to use in our hacky-time travelling machine
In order to scrape for data we need to first download the html page of the site, we use the requests library for this
- Import requests into app.py using `import requests` and of course RequestException `from requests.exceptions import RequestException` which would be used to handle errors
- Define a function called `get_data`.
    i.   Create a variable to hold the site url `site_url="https://www.onthisday.com/"`
    ii.  Get the page data using requests and save it to a variable `res = requests.get(website_url)`
    iii. Catch the `RequestException`  using a try-catch statement.
    iv.  If the exception is thrown return a dictionary with only key 'status' that maps to `False` ie `{"status":False}`
            - Note: `False` is a `boolean` not a `string`

    v.   If the exception does not occur, return a dictionary like so:
    `{"status": True, "content": res.text}`
            - Note: `True` is a `boolean` not a `string`
            -Tip: Remember to change `res` to whatever variable you usedd  


# 3 Getting a list of events(Parsing site data)
   We can get the list of events by parsing through the html contents we got from the previous task, to do we would be using the wonderful BeautifulSoup library.
- First import the BeautifulSoup class from the bs4(version 4 of the BeautifulSoup library) into app.py using `from bs4 import BeautifulSoup`
- Create a function called `get_events`, this function would be receiving only one argument, which we would call  `data`, which is the dictionary gotten from the get_data function.
- Check `status` key of the argument(`data`) passed  ie `data['status']` is equal to `True`, using an if statement.
   - Tip `True` is a `boolean` not a  `string`
- If the check fails, we do nothing and just return `None`.
    - Tip `None` is data type of its own.
- If the check passes, pass `data["content"]` into a new instance  of the `BeautifulSoup` class and save it to a variable eg `soup = BeautifulSoup(data["result"])`
- Next we get the HTML elements that contain the actual events. To do we use the css selector of those elements which is  ".event-list--with-advert>.event", then we pass this
css selector into the "select" method  of `soup`(the variable created in the previous soup) and save it to a variable ie: `events_list = soup.select(".event-list--with-advert>.event")`.

- Return the variable  gotten from the last step.


# 4 Reformatting event list data
While we have successfully scraped for the  events, we need to format in to something more presentable.

- First create, a function called format_events. The format_events function would take only one argument which we call `events` moving forward
- Create a new variable that is actually an empty list. This list would  hold the formatted events we would use `formatted_events`
- Check that `events` argument is not `None`
- If the check passes, we would iterate through the `events` argument using a for loop 
    - Note: We are not going to specify what would happen if check fails, because we would be returning the `formatted_events` regardless
- Inside this for loop, we would do a couple of things
    - Get the year and details of each event by doing  `event_year, event_details = event.text.split(" ", 1)`.
    This bit of code splits each events by the first occurrence of an empty space which is an empty string (`" "`).
    This returns a tuple which contains two elements. The first  element is the year of the event and the second
    element contains details of the event.
    
    - Create a dictionary with two keys
        - The year key is mapped to the `event_year` variable from the previous step
        - The details key is mapped to  the `event_details` variable from the previous step
        
      eg: `event_dict = {year: event_year, details:event_details}`
      - Tip dont change the keys. Use 'year' and 'details' 
    - Append the dictionary(`event_dict`) to the list(`formatted_events`) created in step 2.
- Return the list (`formatted_events`) as the only result of the  `format_events` function.
    - NOte: You need to un-indent  to the first indent of the function ie  `forrmatted_events` and the 
    return are aligned vertically 

# 5 Add visuals, so we can show our time machine
