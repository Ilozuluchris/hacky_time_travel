Welcome to HACKYTIME TRAVEL, a project to help you learn  web scraping by navigating through past events.
Please follow all the instructions and keep an eye out for 

# 1 Setup
- It is advised, you start by creating a virtual environment, personally I use pipenv, but use the method you are most comfortable with.
    - Using pipenv: Install pipenv if you have not via `pip install pipenv`and create the environment via `pipenv shell --python 3`;
-   Install requirements
    - Using pipenv: `pipenv install -r requirements.txt`
- To verify setup run `ptw` or `pytest-watch`, all the tests should be failing, which is what we want. As you go through this project all the tests would pass!

# 2 Getting site data
We would be using `https://www.onthisday.com/` to get the events to use
In order to scrape for data we first need to download the html page of the site, we would use the requests library for this
- Import the `requests` library into app.py using `import requests`
- Then import RequestException via `from requests.exceptions import RequestException` which would be enable us handle errors that the requests library might throw.
- Define a function called `get_data`.
    i.   Create a variable to hold the site url `site_url="https://www.onthisday.com/"`, this site has a list of events that happened on a particular day, in this case today.
    ii.  Get the html data by passing the site_url to `requests.get()` and assigning the result to a variable ie `res = requests.get(site_url)`
    iii. Catch the `RequestException`, this exception can thrown from ii above  using a try-catch statement.
    iv.  If `RequestException` is thrown return a dictionary with only key 'status' that maps to `False` ie `{"status":False}`
            - Note: `False` is `boolean` not a `string`
    v.   If `RequestException` does not occur, return a dictionary like so: `{"status": True, "content": res.text}`
            - Note: `True` is a `boolean` not a `string`
            - Tip: Remember to change `res` to whatever variable you used to store the html data gotten in ii

# 3 Getting a list of events (Parsing site data)
  Since we have gotten data from the site we now need to get a list of events by parsing through the data from the previous task, to do that we would be using the wonderful BeautifulSoup library.
  The BeautifulSoup library allow us makes sense of the html data via code.
- First we import the BeautifulSoup class from the bs4(version 4 of the BeautifulSoup library) into app.py using `from bs4 import BeautifulSoup`
- Next, we create a function called `get_events`, this function would be receiving only one argument called `data`, which is the dictionary returned by the get_data function in the previous task.
- Check the `status` key of the argument(`data`) passed  ie `data['status']` is equal to `True`, using an if statement.
   - Tip `True` is a `boolean` not a  `string`
- If the check fails, we do nothing and just return `None` since this form is not useful to us.
    - Tip `None` is a  data type of its own in python.
- If the check passes, pass `data["content"]` into a new instance  of the `BeautifulSoup` class and save it to a variable eg `soup = BeautifulSoup(data["result"], "html.parser")`
    - Tip: The second argument to the BeautifulSoup constructor tells it what html parser to use, this ensures all machines parse the html the same way. This is very important when you plan to share your code with others or deploy on a different side.
- Next we get the HTML elements that contain the actual events. To do this, we use the css selector of those elements which is  ".event-list--with-advert>.event" which I got via inspecting the page using my browser's dev tools, then we pass this
css selector into the "select" method  of `soup`(the variable created in the previous step) and save it to a variable ie: `events_list = soup.select(".event-list--with-advert>.event")`.

- Return the variable  gotten from the last step.


# 4 Reformatting event list data
While we have successfully scraped for the  events, we need to format in to something more presentable.

- First create, a function called format_events. The format_events function would take only one argument which we call `events` moving forward
- Create a new variable that is actually an empty list. This list would  hold the formatted events we would use `formatted_events`
- Check that `events` argument is not `None`
- If the check passes, we would iterate through the `events` argument using a for loop 
    - Note: We are not going to specify what would happen if check fails, because we would be returning the `formatted_events` regardless
- Inside this for loop, we would do a couple of things
    - Get the year and details of each event by doing  `event_year, event_details = event.text.split(" ", 1)`. `event.text` contain the actual text(inside the HTML tags) from the events html
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
