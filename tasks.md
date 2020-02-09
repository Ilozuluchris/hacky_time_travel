After setting up, you can dive in

# 1 Getting site data
In order to scrape for data we need to first download the html page of the site, we use the requests library for this
- Import requests into app.py using `import requests`
- Define a function called getData.
  - create a variable to hold the site url `site_url="https://www.onthisday.com/"`
  - download the page data using requests `res = requests.get(website_url)`
  -  todo handle exception