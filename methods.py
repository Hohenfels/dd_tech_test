def get_nb_articles(element):
    import re

    regex_match = re.search("全 ([1-9,]+)件", element.text)
    if regex_match:
        return int(regex_match.group(1).replace(',', ''))
    else:
        exit("The element you requested doesn't work or is unavaible")

def get_url(element):
    data = element.find("a", {"target": "_top"})
    return data.get('href')

def get_desc(element):
    data = element.find_all("a", {"target": "_top"})
    return data[2].text

def get_price(element):
    data = element.find("span", {"class": "important"})
    return data.text

def scrap_it(element):
    url = get_url(element)
    print(url)
    desc = get_desc(element)
    print(desc)
    price = get_price(element)
    print(price)
