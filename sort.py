items = [
    ("Product", 10),
    ("Product 2", 15),
    ("Product 3", 25),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

prices = list(map(lambda item: item[1], items))
print(prices)
