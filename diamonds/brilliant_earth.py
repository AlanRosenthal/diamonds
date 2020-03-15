"""
get data from Brilliant Earth
"""

import urllib.parse, urllib.request
import json
import diamonds.store


def generate_url(page=1, color="D,E,F,G,H,I,J", sort_by="asc", shape="All", clarity="SI2,SI1,VS2,VS1,VVS2,VVS1,IF,FL", cut="Fair,Good,Very Good,Ideal,Super Ideal"):
    BASE_URL = "https://www.brilliantearth.com/loose-diamonds/list/?"
    params = {
        "row": "0",
        "page": f"{page}",
        "requestedDataSize": "200",
        "shapes": f"{shape}",
        "order_by": "price",
        "order_method": f"{sort_by}",
        "currency": "$",
        "cuts": f"{cut}",
        "colors": f"{color}",
        "clarities": f"{clarity}",
    }
    return BASE_URL + urllib.parse.urlencode(params)


def query(page, color, sort_by, shape, clarity, cut):
    req = urllib.request.Request(generate_url(page, color, sort_by, shape, clarity, cut))
    with urllib.request.urlopen(req) as response:
        raw_data = response.read()
        json_data = json.loads(raw_data.decode("utf-8"))
        if "diamonds" in json_data:
            return json_data["diamonds"]
        return []


def download(page_start, page_end, color, sort_by, shape, clarity, cut):
    for page in range(page_start, page_end):
        db_count_before = diamonds.store.count_entries()
        data = query(page, color, sort_by, shape, clarity, cut)
        print("Total entries downloaded (page: {}): {}".format(page, len(data)))
        for diamond in data:
            diamonds.store.insert_unique_data(
                diamond["upc"],
                diamond["shape"],
                diamond["price"],
                diamond["carat"],
                diamond["clarity"],
                diamond["cut"],
                diamond["color"],
            )
        db_count_after = diamonds.store.count_entries()
        print(
            "Total entries in DB: {DB_COUNT}, new entries: {DELTA}".format(
                DB_COUNT=db_count_after, DELTA=db_count_after - db_count_before
            )
        )
