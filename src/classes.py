class Category:
    """
    Класс категорий товаров
    name: название
    description: описание
    products: товары(список объектов класса  Product)
    """

    name: str
    description: str
    __products: list

    category_quantity = 0
    unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_quantity += 1

    def add_product(self, new_product):
        """
        Метод для добавления товара в категорию
        """
        if not isinstance(new_product, Product):
            print("Ошибка: Неверный тип товара")
            Category.unique_products = len(set(self.__products))
            return
        else:
            self.__products.append(new_product)
            Category.unique_products = len(set(self.__products))

    @property
    def products(self):
        products_info = []
        for product in self.__products:
            products_info.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return "\n".join(products_info)

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

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Ошибка: Цена должна быть больше нуля")
        else:
            self.__price = value



# # Создаем экземпляр класса Product
# # product1 = Product.create_product("Товар 1", "Описание товара 1", 50.0, 20)
# # product2 = Product.create_product("Товар 2", "Описание товара 2", 80.0, 15)
# #
# # # Создаем экземпляр класса Category и добавляем в него продукты
# # category = Category("Категория 1", "Описание категории 1", [product1, product2])
# #
# # # Выводим информацию о продуктах в категории
# # print(category.products)