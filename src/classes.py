class Category:
    """
    Класс категорий товаров
    name: название
    description: описание
    products: товары
    """

    name: str
    description: str
    __products: list

    category_quantity = 0
    unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_quantity += 1
        Category.unique_products = len(set(products))

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.unique_products = len(set(self.__products))

    @property
    def products(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'


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
        self.__price = price
        self.quantity = quantity

    @staticmethod
    def create_product(name, description, price, quantity):
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Ошибка: Цена должна быть больше нуля")
        else:
            self.__price = value



