from src.abstract_classes import Prod
from src.mixins import MixinInfo


class Category(MixinInfo):
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
        MixinInfo.__init__(self)
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
        elif new_product.quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            self.__products.append(new_product)
            Category.unique_products = len(set(self.__products))

    @property
    def products(self):
        """
        Метод для вывода информации о товаре
        """
        products_info = []
        for product in self.__products:
            products_info.append(str(product))
        return "\n".join(products_info)

    def average_price(self):
        '''
        метод, который подсчитывает средний ценник всех товаров
        исключение - когда в категории нет товаров и сумма всех товаров будет делиться на ноль.
        в случае, если такое происходит, возвращает ноль
        '''
        sum_price = 0
        for product in self.__products:
            sum_price += product.price
        try:
            average_price = sum_price / len(self.__products)
        except ZeroDivisionError:
            average_price = 0
            return average_price
        else:
            return average_price


class Product(Prod, MixinInfo):
    """
    Класс товаров
    name: название
    description: описание
    price: цена
    quantity: количество в наличии
    color: цвет
    """

    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        MixinInfo.__init__(self)

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return (self.price*self.quantity) + (other.price*other.quantity)
        raise TypeError

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


class Smartphone(Product):
    """
    Класс смартфон (наследуется от класса Product)
    name: название
    description: описание
    price: цена
    quantity: количество в наличии
    color: цвет
    performance: производительность
    model: модель
    memory: объём памяти
    """

    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        self.performance = performance
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)



class LawnGrass(Product):
    """
    Класс трава газонная (наследуется от класса Product)
    name: название
    description: описание
    price: цена
    quantity: количество в наличии
    color: цвет
    country: страна-производитель
    period: срок прорастания
    """

    def __init__(self, name, description, price, quantity, color, country, period):
        self.country = country
        self.period = period
        super().__init__(name, description, price, quantity, color)


# class Order:
#
#     def __init__(self):
#         pass
#

# prod1 = Product("Товар 1", "Описание товара 1", 50.0, 2)
# prod2 = Product("Товар 2", "Описание товара 2", 60.0, 2)
# # smart1 = Smartphone("Смартфон", "Описание товара", 60.0, 20, "синий", 100, "A120", "128 Mb")
# # grass1 = LawnGrass("Трава", "Описание травы", 1.0, 10, "зеленая", "Голландия", "10 дней")
# category1 = Category("Категория", "Описание")
# category1.add_product(prod1)
# category1.add_product(prod2)
# print(category1.average_price())