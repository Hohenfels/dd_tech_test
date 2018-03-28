# coding=utf_8

def get_nb_articles(element):
    import re

    if element:
        regex_match = re.search("全 ([1-9,]+)件", element.text)
        if regex_match:
            return int(regex_match.group(1).replace(',', ''))
        else:
            exit("The element you requested doesn't work or is unavailable")
    else:
        exit(Element doesn't exist)

def get_url(element):

    data = element.find("a", {"target": "_top"})
    return data.get('href')

def get_desc(element):

    data = element.find_all("a", {"target": "_top"})
    return data[2].text

def get_price(element):

    data = element.find("span", {"class": "important"})
    return data.text.strip('円').replace(",", "") + " CPY"

def get_picture(element):

    data = element.find("img", {"class": "_verticallyaligned"})
    return data.get('src')

def get_seller_name(element):

    data = element.find_all("a", {"target": "_top"})
    return data[1].text

def get_seller_url(element):

    data = element.find_all("a", {"target": "_top"})
    return data[1].get('href')

def write_to_csv(table, brand):

    import csv
    import os.path
    import uuid

    brand = brand.replace(" ", "_").lower()
    folder = brand
    if os.path.isdir("csv/" + folder) is False:
        os.makedirs("csv/" + folder)
    file_path = "csv/" + folder + "/" + brand + "_" + str(uuid.uuid1()) + ".csv"

    if os.path.isfile(file_path) is False:
        open(file_path, 'a').close()
    file = open(file_path, "a", encoding = "utf-8")

    writer = csv.writer(file, delimiter = "\n")
    writer.writerow((
        "URL ", table["UR"] + "\n",
        "Description ", table["DC"] + "\n",
        "Price ", table["PR"] + "\n",
        "Picture URL ", table["PU"] + "\n",
        "Seller name ", table["SN"] + "\n",
        "Seller URL ", table["SU"] + "\n"))

def scrap_it(element):

    price = get_price(element)
    url = get_url(element)
    desc = get_desc(element)
    picture = get_picture(element)
    seller_name = get_seller_name(element)
    seller_url = get_seller_url(element)

    table = {
        "UR": url,
        "DC": desc,
        "PR": price,
        "PU": picture,
        "SN": seller_name,
        "SU": seller_url
    }

    return table
