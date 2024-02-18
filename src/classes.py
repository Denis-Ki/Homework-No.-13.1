class Category:
    """
    Класс категорий товаров
    name: название
    description: описание
    products: товары
    """

    name: str
    description: str
    products: list

    category_quantity = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_quantity += 1
        Category.unique_products = len(set(products))


class Product:
    """
    Класс товаров
    name: название
    description: описание
    price: цена
    quantity: количество в наличии
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
