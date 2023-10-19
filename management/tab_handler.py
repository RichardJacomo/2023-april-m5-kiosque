from menu import products


def calculate_tab(table):
    values = []
    total = 0
    for item in products:
        for item_table in table:
            if item["_id"] == item_table["_id"]:
                values.append(item_table["amount"] * item["price"])
    for value in values:
        total += value   
    return {"subtotal": (f"${round(total, 2)}")}