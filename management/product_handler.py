from menu import products


def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for index in products:
        if id == index["_id"]:
            return index
    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    filtered = [n for n in products if n["type"] == type]
    return filtered if filtered else []


def add_product(menu, **kwargs):
    max_value_id = 0
    for item in menu:
        if item["_id"] > max_value_id:
            max_value_id = item["_id"]
    product = kwargs
    product["_id"] = max_value_id + 1 if menu else 1    
    menu.append(product)
    return product


def menu_report():
    total_average_price = sum(n["price"] for n in products)
    types = [n["type"] for n in products]
    dict_types = {n: types.count(n) for n in types}
    most_common = max(dict_types, key=dict_types.get)
    return (f"Products Count: {len(products)} \
- Average Price: ${round(total_average_price / len(products), 2)} \
- Most Common Type: {most_common}")