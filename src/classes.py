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

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        return len(self.__products)

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
            products_info.append(str(product))
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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.price*self.quantity) + (other.price*other.quantity)

    @classmethod
    def create_product(cls, name, description, price, quantity, existing_products=None):
        """
        Создает новый экземпляр продукта с учетом возможных дубликатов.
        """
        if existing_products is None:
            existing_products = []

        # Поиск дубликата по имени в существующих продуктах
        for existing_product in existing_products:
            if existing_product.name == name:
                # Дубликат найден
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)  # Выбираем более высокую цену
                return existing_product

        # Дубликат не найден, создаем новый продукт
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Ошибка: Цена должна быть больше нуля")
            return
        if value < self.__price:
            # Цена понижается, запрашиваем подтверждение пользователя
            confirmation = input(f"Цена товара {self.name} понижается. Принять изменение? (y/n): ")
            if confirmation.lower() == 'n':
                return
        self.__price = value



