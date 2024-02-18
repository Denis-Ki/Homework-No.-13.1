import pytest
from src.classes import Category, Product


@pytest.fixture
def category_electronics():
    return Category('Электроника', 'Изделия электронной промышленности', ['телевизор', 'сотовый телефон', 'наушники', 'телевизор'])


@pytest.fixture
def products_mobile():
    return Product('Iphone SE', 'Смартфоны, сотовые телефоны', 19500.50, 6)


def test_category_init(category_electronics):
    assert category_electronics.name == 'Электроника'
    assert category_electronics.description == 'Изделия электронной промышленности'
    assert category_electronics.products == ['телевизор', 'сотовый телефон', 'наушники', 'телевизор']
    assert Category.category_quantity == 1
    assert Category.unique_products == 3


def test_product_init(products_mobile):
    assert products_mobile.name == 'Iphone SE'
    assert products_mobile.description == 'Смартфоны, сотовые телефоны'
    assert products_mobile.price == 19500.50
    assert products_mobile.quantity == 6
