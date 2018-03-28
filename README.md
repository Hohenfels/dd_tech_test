# Data & Data technical challenge

## Introduction

A technical challenge about making a web-scraping program written in Python ( >= 3).
This web-scrapper wad built to scrap Rakuten.co.jp
Thought it's not including every handbags for certain brand because of the pagination limit (150).

To realize this project I started thinking about the structure of a website.
Every articles in a search request are just template filled with the right information.
So to scrap that, I juste found the right element of each informations then wrote it to a csv file.
Every file corresponds to an article (yep... you can basically have 10M files with this program).
I made it generic so you can basically find any handbags according to a brand if it exists on Rakuten.co.jp and it's also gonna ask you how much page you wanna scrap.
After that , I decided to not make any class for the articles because it wasn't necessary, and also because of the lack of time I got to realize this. I tried to do something just fine, but I could easily improve this.

## Code Samples

The most important part of the program is this one :

This 'while True' loop gonna increment until the number of page to scrap is reached.
For each incrementation, i'm gonna request the right page according to i.
Then I parse my html page and send it to a function 'scrap_it()' which gonna parse the inner element of the actual div and retrieve data needed for the project.
Then i'm gonna write the data for the actual page into a .csv file so every article has a unique .csv.
 ```
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
```
To decide what brand the user wants to scrap, the program just ask simply and retrieve an input and will create a first link for the next step. (more details in the comment inside my code)
```
website = "https://search.rakuten.co.jp/search/mall/"

brand_to_search = input("What brand would you like to scrap on Rakuten.co.jp ?\n")
brand_formatted = brand_to_search.replace(" ", "+")

final_url = website + brand_formatted + "+handbags/?p=1"
```
Then i'm gonna calculate the exact numbers of page by dividing the number of articles (scrapped a first time with the URL I made before) with the number of items per page and then I do a control to check if the number of page isn't above the limit (150).

example : 3600 / 45 (rounded to the lowest decimal to be precise)
```
request = requests.get(final_url)
soup = BeautifulSoup(request.content, "html.parser")

articles = soup.find_all("div", {"class": "dui-card searchresultitem"})
max_pages = math.trunc(get_nb_articles(soup.find("h1", {"class": "section"})) / 45) + 1
if max_pages > 150:
    max_pages = 150
```

Then I ask the user about how much page does he wants to scrap according to the max number
```
nb_page = input("How much page ? (max for " + brand_to_search + " is " + str(max_pages) + ")\n")
nb_page = int(nb_page)
if nb_page > max_pages:
    print("You entered a number of pages above the max page number\n\
            Then, your default value will be " + str(max_pages))
    nb_page = max_pages
```

## Installation

To run the program make sure you've launched the install.sh by doing "sh install.sh" on unix system or "pip install beautifulsoup4 requests", it is gonna install the dependencies to make the program works.

It is gonna install BeautifulSoup 4 and requests.
