# TASK1: Import any library you think you'll need to scrape a website

import requests
import bs4

# TASK2: Use requests libraryand BeautifulSoup to connect to http://quotes.toscrape.com/ 
# and get the HTML text from the homepage

base_url = 'http://quotes.toscrape.com/page/{}/'
scrape_url = base_url.format(1)
req =  requests.get(scrape_url)
soup = bs4.BeautifulSoup(req.text, 'lxml')
print(soup)
print("\n")

# TASK3: Get the names of all the authors on the first page

soup.select('.author')
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)
print(authors)
print("\n")

# TASK4: Create a list of all the quotes on the first page

soup.select(".text")
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)
print("\n")

# TASK5: Inspect the site and use BeautifulSoup to extract the top ten tags from the requests text shown on the top right
# from the home page(e.g.- Love, Inspirational, Life, etc..)
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, 
# perhaps check the span

soup.select(".tag-item")
for tags in soup.select(".tag-item"):
    print(tags.text)
print("\n")

# TASK6: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors 
# on the website. 
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that 
# your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, 
# so the last page is http://quotes.toscrape.com/page/10/, 
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, 
# perhaps use try/except for this, its up to you!

url = "http://quotes.toscrape.com/page/"
page_still_valid = True
authors = set()
page = 1
while page_still_valid:
    page_url = url + str(page) 
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

    page = page + 1

print(authors)
