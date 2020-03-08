"""
"""

import diamonds.store
import plotly
import plotly.graph_objs as go
import plotly.express as px


def get_group(diamond):
    cut = diamond[5].replace(" ", "")
    return f"{diamond[4]}_{diamond[6]}_{cut}"


def graph(carat, shape, color, clarity, cut):
    color_list = color.split(",")
    clarity_list = clarity.split(",")
    cut_list = cut.split(",")
    diamonds_from_store = diamonds.store.query_db(
        carat[0], carat[1], shape, color_list, clarity_list, cut_list
    )
    print(f"diamonds: {len(diamonds_from_store)}")

    data = {}
    for diamond in diamonds_from_store:
        group = get_group(diamond)
        if group not in data:
            data[group] = []
        data[group].append(
            {"key": diamond[0], "price": diamond[2], "size": diamond[3],}
        )

    print(f"groups: {len(data)}")

    # fig = go.Figure()
    # add_datasets_to_figure(fig, data)
    # plotly.offline.plot(fig)


def add_datasets_to_figure(fig, data):
    for group in data:
        price = []
        size = []
        for x in data[group]:
            price.append(x["price"])
            size.append(x["size"])
        fig.add_trace(go.Scatter(x=price, y=size, mode="lines+markers", name=group))
