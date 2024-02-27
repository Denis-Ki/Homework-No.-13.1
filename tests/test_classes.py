import pytest
from src.classes import Category, Product


@pytest.fixture
def category_electronics():
    return Category('Электроника', 'Изделия электронной промышленности', ['телевизор', 'сотовый телефон', 'наушники', 'телевизор'])


@pytest.fixture
def category_electronics1():
    return Category('Test category', 'Test description', [])


@pytest.fixture
def products_mobile():
    return Product('Iphone SE', 'Смартфоны, сотовые телефоны', 19500.50, 6)


def test_category_init(category_electronics):
    assert category_electronics.name == 'Электроника'
    assert category_electronics.description == 'Изделия электронной промышленности'
    assert category_electronics._Category__products == ['телевизор', 'сотовый телефон', 'наушники', 'телевизор']
    assert Category.category_quantity == 1
    assert Category.unique_products == 3


def test_product_init(products_mobile):
    assert products_mobile.name == 'Iphone SE'
    assert products_mobile.description == 'Смартфоны, сотовые телефоны'
    assert products_mobile._Product__price == 19500.50
    assert products_mobile.quantity == 6


def test_category_add_product(category_electronics, products_mobile):
    initial_product_count = len(category_electronics._Category__products)

    category_electronics.add_product(products_mobile.name)

    assert len(category_electronics._Category__products) == initial_product_count + 1
    assert Category.unique_products == 4  # С учетом уникальных товаров


def test_category_products_property(category_electronics1, products_mobile):
    category_electronics1.add_product(products_mobile)

    expected_output = f"{products_mobile.name}, {products_mobile.price} руб. Остаток: {products_mobile.quantity} шт."

    assert category_electronics1.products == expected_output


def test_product_create_product():
    new_product = Product.create_product("Test Product", "Test Description", 30.0, 5)

    assert isinstance(new_product, Product)
    assert new_product.name == "Test Product"
    assert new_product.price == 30.0
    assert new_product.quantity == 5


def test_product_price_setter():
    test_product = Product("Test Product", "Test Description", 50.0, 10)

    test_product.price = 60.0
    assert test_product.price == 60.0


if __name__ == "__main__":
    pytest.main()