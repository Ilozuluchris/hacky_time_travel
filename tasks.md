Hi and welcome again, please go through this tasks carefully, good luck!\
Task 1 and 2 would guide you in getting a list of events via scraping a website, then task 3 and 4 would guide you in building the hacky time machine.\
You would need to touch only one file `app.py`, which should be empty at this point.

# 1 Getting site data
We would be getting our events from `https://www.onthisday.com/`   
But before we can get our events, we need to first download the html page of the site, we would use the requests library for this.
- Import the `requests` library into app.py using `import requests`
- Then import `RequestException` via `from requests.exceptions import RequestException` which would be enable us handle errors that the requests library might throw.
- Next define a function called `get_data`. Inside the function do the following:
    1. Create a variable to hold the site url ie. `site_url="https://www.onthisday.com/"`, this site has a list of events that happened on a particular day, in this case today.
       - Tip: Pay attention to the url scheme(`https`) and the www part.
    2. Get the html data by passing the site_url to `requests.get()` and assigning the result to a variable ie `res = requests.get(site_url)`
    3. Catch the `RequestException`, this exception can thrown from the code in the previous step, using a try-catch statement.
    4.  If `RequestException` is thrown return a dictionary whose only key('status') maps to `False` ie `{"status":False}`
            - Note: `False` is `boolean` not a `string`
    5.   If `RequestException` does not occur, return a dictionary like so: `{"status": True, "content": res.text}`
            - Note: `True` is a `boolean` not a `string`
            - Tip: Remember to change `res` to whatever variable you used to store the html data gotten in ii

# 2 Getting a list of events (Parsing site data)
  Now that we have gotten data from the site we now need to get a list of events by parsing through the data from the previous task, to do that we would be using the wonderful BeautifulSoup library.
  The BeautifulSoup library would allow us makes sense of  (parsing) the html data.
- First we import the BeautifulSoup class from the bs4(version 4 of the BeautifulSoup library) into app.py using `from bs4 import BeautifulSoup`
- Next, we define a function called `get_events`, this function would be receiving only one argument called `data`, which is the dictionary returned by the `get_data` function in the previous task.
- Check the `status` key of the argument(`data`) passed  ie `data['status']` is equal to `True`, using an if statement.
  - Tip: `True` is a `boolean` not a  `string`
- If the check fails, we do nothing and just return `None` since this case is not useful to us.
    - Tip: `None` is a  data type of its own in python.
- If the check passes, pass `data["content"]` into a new instance  of the `BeautifulSoup` class and save it to a variable ie. `soup = BeautifulSoup(data["result"], "html.parser")`
    - Tip: The second argument to the BeautifulSoup constructor tells it what html parser to use, this ensures all machines parse the html the same way. This is very important when you plan to share your code with others or deploy on a different machine.
- Next we get the HTML elements that contain the actual events. To do this, we use the css selector of those elements which is `.event-list--with-advert>.event` which I got via inspecting the page using my browser's dev tools, then we pass this
css selector into the "select" method  of `soup`(the variable created in the previous step) and save it to a variable ie: `events_list = soup.select(".event-list--with-advert>.event")`.

- Return the variable  gotten from the last step as the only result of the `get_events` function.

# 3 Formatting the list of events
While we have successfully scraped for a list of  events, hurray! We need to format it to something more parsable for our time machine.
- First we create, a function called `format_events`. The format_events function would take only one argument which we would call `events` moving forward.
- Create a new variable called `formatted_events` which is really an empty list for now but would hold the formatted events.
- Check that `events` (the argument to format_events) argument is not `None`
- If the check passes, we would iterate through the `events` argument using a for loop 
    - Note: We are not going to specify what would happen if check fails, because we would be returning the `formatted_events` irregardless
- Inside this for loop, we would do a couple of things:
    1. Get the year and details of each event using `event_year, event_details = event.text.split(" ", 1)`. `event.text` contains the actual text(inside the HTML tags) from the events html.\
       This line of code splits each event into its year of occurrence and details using  the first appearance of an empty space (which is an empty string in python).
       This returns a tuple which contains two elements whose first  element is the year the event occurred and the second
       element contains details of the event.
    2. Create a dictionary with two keys
        - The `year` key which would be  mapped to the `event_year` variable from the previous step
        - The `details` key which would be mapped to  the `event_details` variable from the previous step    
        The resulting dictionary would look like so `event_dict = {year: event_year, details:event_details}`
            - Tip: Don't change the keys. Use `year` and `details` this is very important for the next task 
    3. Append the dictionary(`event_dict`) from the previous step to the list(`formatted_events`) created previously.
- Return the list (`formatted_events`) as the only returned value of the `format_events` function.
    - Tip: You need to un-indent to the first indent level of the `format_events` function
    before returning the result, this ensures all the formatted events are in the list not just one

# 4 Putting it all together (Forming a hacky time machine)
Congrats on making it this far, hopefully with no bugs, we are done with the web scraping part
but we need to tie it all together and create our hacky time machine, after all there is no time travel
without a time machine. To build our time machine we would use flask, which is a web framework for python.
As this task focuses heavily on flask and not web scraping I would rapidly gloss over the code, you only need to copy and paste  the code.

- Import the needed Flask libraries using `from flask import Flask, render_template`

-   Next copy and paste this into `app.py`
    `````python
    flask_app = Flask(__name__)
    
    
    @flask_app.route('/')
    def hello_world():
        page_data = get_page_data()
        events_in_history = format_events(get_events(page_data))
        return render_template('index.html', events=events_in_history)
    
    ````` 
    This block of code creates a flask application, then defines what happens when we visit
    the index page(`\`) of the app, which in this case is getting a list of our formatted events
    and rendering it on a html page.

-   Next we write the code for starting the flask app, this block should be the last thing in the `app.py` file.
    ```python
    if __name__ == "__main__":
        flask_app.run('0.0.0.0', 5000, True)
    
    ```
    This block of code basically states that our flask app should start/listen on port 5000 of our local machine in debug mode.
    The use of `if __name__ == "__main__"` ensures the app only starts when the script is ran
    - Tip: If port 5000 of your machine is not open, feel free to change it as needed.

-   Run `python app.py` to time travel, play around the page and enjoy!
