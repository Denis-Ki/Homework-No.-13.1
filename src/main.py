import json
from classes import Category, Product


def main():
    """
    подгрузка данных по категориям и товарам из файла JSON
    """

    with open('products.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    categories = []
    products = []

    for category_data in data:
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
            products.append(product)

        category = Category(category_data['name'], category_data['description'], products)
        categories.append(category)


if __name__ == '__main__':
    main()
