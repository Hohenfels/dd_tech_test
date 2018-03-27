def get_nb_articles(element):
    import re

    regex_match = re.search("全 ([1-9,]+)件", element.text)
    if regex_match:
        return int(regex_match.group(1).replace(',', ''))
    else:
        exit("The element you requested doesn't work or is unavaible")
