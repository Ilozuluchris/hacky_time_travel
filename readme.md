# Introduction
Welcome to Hacky time travel! This project is designed to introduce you to web scraping with python.
Together we are going to get noteworthy events that happened
today, by scraping a website (web scraping), and go through them in chronologically order thereby giving
us a "time travel" experience.

## Prerequisites
- Some python knowledge.
- Basic HTML and CSS (to be particular CSS selectors) knowledge.
- Python 3 installed, preferable python 3.8 but any version from 3.6+ should work
- A code editor.

## Setup
- Navigate to the root folder of the project.
- Install requirements in requirements.txt preferably in a virtual environment, personally I recommend [Pipenv](https://pipenv.pypa.io/en/latest/)
  - Using Pipenv: `pipenv install -r requirements.txt --three` then activate the virtual environment using `pipenv shell`.
-  Run `ptw` or `pytest-watch` on your terminal to verify the setup, all tests should fail, which is a good thing. Keep this running, so we can watch the tests pass as we progress.

## What Next?
Once you are done with the setup, feel free to dive into the tasks.

## Some tips for tasks
- Pay attention to the function names mentioned in tasks, **do not change them** unless the tests would never pass
- If you use different variables from those listed in the tasks, ensure you stick to the new names you use in later steps.
- Pay attention to strings(and the lack of strings) especially those that appear inside backticks(``).
- Don’t change the keys of dictionaries mentioned in tasks, unless the tests would never pass.

### Miscellaneous

- Why Pipenv?
  1. Simpler commands to manage the virtual environment, eg. you don't need to remember the name of your virtual environment to activate it.
  2. Better dependency management.

- Why Requests?
  1. A more human-readable API than urllib.

- Ways to improve code
  1. If you included an else statement in the get_events function in task 2
You can actually remove this. Tip: In python, functions return None by default
