import os, sys
import csv
import requests
import math
from methods import scrap_it, get_nb_articles, write_to_csv
from bs4 import BeautifulSoup

# First of all, make sure you have installed BeautifulSoup and reauests (see the README.txt), thank you ! Felicien RENAUD @ 42

# I made this technical test to be generic, so you can search any brand on Rakuten.co.jp
def main():
    website = "https://search.rakuten.co.jp/search/mall/"

    brand_to_search = input("What brand would you like to scrap on Rakuten.co.jp ?\n")
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

    max_pages = math.trunc(get_nb_articles(soup.find("h1", {"class": "section"})) / 45) + 1
    if max_pages > 150:
        max_pages = 150

    # Now asking the user how much pages he wants to scrap

    nb_page = input("How much page ? (max for " + brand_to_search +" is " + str(max_pages) + ")\n")
    nb_page = int(nb_page)
    if nb_page > max_pages:
        print("You entered a number of pages above the max page number\n\
                Then, your default value will be " + str(max_pages))
        nb_page = max_pages

    # Here is the big part, a big loop that's gonna retrieve every articles from N page(s)
    # I begin to find all the article with soup.find_all according to the right div
    # I do a for loop to get inside every div and begin the extraction of data
    # then I write my data to a .csv file with the name of the brand requested

    i = 1
    while True:
        final_url = website + brand_formatted + "+handbags/?p=" + str(i)
        request = requests.get(final_url)
        soup = BeautifulSoup(request.content, "html.parser")
        articles = soup.find_all("div", {"class": "dui-card searchresultitem"})
        for article in articles:
            table = scrap_it(article)
            write_to_csv(table, brand_to_search)
        if i == nb_page:
            break
        i += 1

if __name__ == "__main__":
    main()