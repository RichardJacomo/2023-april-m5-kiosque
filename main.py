from management.product_handler import get_product_by_id, \
                                      get_products_by_type, \
                                      add_product, \
                                      menu_report \


from management.tab_handler import calculate_tab
from menu import products


if __name__ == "__main__":

    # print(get_product_by_id(25))
    # print(get_products_by_type(1))

    # new_product = {
    #     "title": "X-Python",
    #     "price": 5.0,
    #     "rating": 5,
    #     "description": "Sanduiche de Python",
    #     "type": "fast-food"
    # }
    # print(add_product(products, **new_product))

    # table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    # print(calculate_tab(table_1))

    print(menu_report())
    ...