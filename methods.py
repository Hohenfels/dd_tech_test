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
    import pandas as pd

    brand = brand.replace(" ", "_").lower()
    file_path = "csv/" + brand + ".csv"
    df = pd.DataFrame(table, columns = ["Url", "Description", "Price", "Seller name", "Seller URL"], index = [0])

    if os.path.isfile(file_path) is False:
        open(file_path, 'a').close()
    with open(file_path, 'a') as file:
        df.to_csv(file, header = False)
    # with open(file_path, "w", encoding = "utf-8") as file:
    #     writer = csv.writer(file, delimiter = " ")
    #     writer.writerow(table["UR"])
    #     writer.writerow(table["DC"])
    #     writer.writerow(table["PR"])
    #     writer.writerow(table["PU"])
    #     writer.writerow(table["SN"])
    #     writer.writerow(table["SU"])
    # file.close()
        
def scrap_it(element):
    url = get_url(element)
    desc = get_desc(element) 
    price = get_price(element)
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