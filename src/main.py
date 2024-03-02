import json
from classes import Category, Product


def main():
    """
    подгрузка данных по категориям и товарам из файла JSON
    создание списка categories объектов класса Category, содержащих список
    объектов класса Product
    вывод данных на экран
    """

    with open('products.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
            category.add_product(product)

        print(f'{category.name}\n{category.description}\n{category.products}')
        categories.append(category)


if __name__ == '__main__':
    main()
