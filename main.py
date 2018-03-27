import os, sys
import csv
import requests
import math
import pandas as pds
from methods import *
from bs4 import BeautifulSoup

# First of all, make sure you have installed BeautifulSoup and reauests (see the README.txt), thank you ! Felicien RENAUD @ 42

# I made this technical test to be generic, so you can search any brand on Rakuten.co.jp

website = "https://search.rakuten.co.jp/search/mall/"

brand_to_search = input("What brand would you like to scrap on Rakuten.co.jp ? ")
brand_formatted = brand_to_search.replace(" ", "+") # Replacing all the space with '+' to imitate rakuten.co.jp url style

# The final url is divided in 3 parts :     
#                                           - 'website' (https://search.rakuten.co.jp/search/mall/)
#                                           - 'brand name' (equal to the input of the user)
#                                           - '+handbag/?p=1' to only search for handbags and '?p=1' to start at page one
#
# example : https://search.rakuten.co.jp/search/mall/Gucci+handbags/?p=42

final_url = website + brand_formatted + "+handbags/?p=1"

# Doing a simple request with the final URL and getting the content with BS, that, a first time to get the number of articles for the actual request

request = requests.get(final_url)
soup = BeautifulSoup(request.content, "html.parser")

articles = soup.find_all("div", {"class": "dui-card searchresultitem"})

# Retrieving number of articles with the method get_nb_articles and dividing it by 45 (number of article per page) the maximum is 150

nb_articles = math.trunc(get_nb_articles(soup.find("h1", {"class": "section"})) / 45) + 1
if nb_articles > 150:
    nb_articles = 150

# Here is the big part, a big loop that's gonna retrieve every articles from N page(s)
# I begin to find all the article with soup.find_all according to the right div
# then I do a for loop to get inside every div and begin the extraction of data

i = 1
while True:
    final_url = website + brand_formatted + "+handbags/?p=" + str(i)
    request = requests.get(final_url)
    soup = BeautifulSoup(request.content, "html.parser")
    articles = soup.find_all("div", {"class": "dui-card searchresultitem"})
    for article in articles:
        article_url = soup.find("a", {"class": "_top"})
        print (article_url)
    if i == 2:
        break
    i += 1