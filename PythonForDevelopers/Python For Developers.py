# ==================================================

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# ---------------------------------------------------

# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
print(df)

# Plot first column of df
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

# -------------------------------------

import pandas as pd

url  = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

xls = pd.read_excel(url, sheet_name=None)

print(xls.keys())

print(xls['1700'].head())

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request("https://campus.datacamp.com/courses/1606/4135?ex=2")

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()


# ------------------------------------

from urllib.request import urlopen, Request

url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

request = Request(url)

response = urlopen(request)

html = response.read()

print(html)

response.close()

# ------------------------------------

import requests 

url = "http://www.datacamp.com/teach/documentation"

r = requests.get(url)

text = r.text

print(text)

# ------------------------------------

# Import packages
import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

pretty_soup = soup.prettify()

print(pretty_soup)


# -----------------------------------------------


import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

guido_title = soup.title

print(guido_title)

guido_text = soup.get_text()

print(guido_text)


# -------------------------------------------------

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

print(soup.title)

a_tags = soup.find_all("a")

for link in a_tags:
    print(link.get('href'))

# -------------------------------------------------

import requests

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

r = requests.get(url)

json_data = r.json()      # This will parse the JSON response

for k in json_data:
    print(f"{k}: {json_data[k]}") # This will print all key-value pairs in the JSON response

# -------------------------------------------------

import requests

url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

r = requests.get(url)

json_data = r.json()

pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


# -------------------------------------------------

import json

tweets_data_path = 'tweets.txt'

tweets_data = []

tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
     tweet = json.loads(line)
     tweets_data.append(tweet)

tweets_file.close()

print(tweets_data[0].keys())

# -------------------------------------------------