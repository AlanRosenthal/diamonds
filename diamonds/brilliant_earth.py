"""
get data from Brilliant Earth
"""

import urllib.parse, urllib.request
import json
import diamonds.store

def generate_url(page=1, color="J,F,G,I,E,D,H", sort_by="asc"):
    BASE_URL = "https://www.brilliantearth.com/loose-diamonds/list/?"
    params = {
        "row": "0",
        "page": f"{page}",
        "requestedDataSize": "200",
        "shapes": "All",
        "order_by": "price",
        "order_method": f"{sort_by}",
        "currency": "$",
        "cuts": "Fair,Good,Very Good,Ideal,Super Ideal",
        "colors": f"{color}",
        "clarities": "SI2,SI1,VS2,VS1,VVS2,VVS1,IF,FL",
    }
    return BASE_URL + urllib.parse.urlencode(params)

def query(page, color, sort_by):
    req = urllib.request.Request(generate_url(page, color, sort_by))
    with urllib.request.urlopen(req) as response:
        raw_data = response.read()
        json_data = json.loads(raw_data.decode("utf-8"))
        if "diamonds" in json_data:
            return json_data["diamonds"]
        return []

def download(start, end, color, sort_by):
    for page in range(start, end):
        data = query(page, color, sort_by)
        print("Total entries downloaded (page: {}): {}".format(page, len(data)))
        for diamond in data:
            diamonds.store.insert_unique_data(diamond["upc"], diamond["shape"], diamond["price"], diamond["carat"], diamond["clarity"], diamond["cut"], diamond["color"])
        print("Total entries in DB: {}".format(diamonds.store.count_entries()))
