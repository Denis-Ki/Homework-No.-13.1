import pytest
from src.classes import Category, Product
from unittest.mock import patch

@pytest.fixture
def empty_category():
    return Category("Категория", "Описание")


@pytest.fixture
def sample_product():
    return Product.create_product("Товар", "Описание товара", 50.0, 10)


def test_category_init(empty_category):
    assert empty_category.name == "Категория"
    assert empty_category.description == "Описание"
    assert empty_category._Category__products == []
    assert Category.category_quantity == 1
    assert Category.unique_products == 0


def test_add_product_valid(empty_category, sample_product):
    empty_category.add_product(sample_product)
    assert empty_category._Category__products == [sample_product]
    assert Category.unique_products == 1


def test_add_product_invalid_type(empty_category):
    non_product = "Не продукт"
    empty_category.add_product(non_product)
    assert empty_category._Category__products == []
    assert Category.unique_products == 0


def test_products_property_empty_category(empty_category):
    assert empty_category.products == ""


def test_products_property_with_products(empty_category, sample_product):
    product1 = Product.create_product("Товар 1", "Описание товара 1", 50.0, 20)
    product2 = Product.create_product("Товар 2", "Описание товара 2", 80.0, 15)
    empty_category.add_product(product1)
    empty_category.add_product(product2)
    assert empty_category.products == "Товар 1, 50.0 руб. Остаток: 20 шт.\nТовар 2, 80.0 руб. Остаток: 15 шт."


def test_product_init():
    product = Product("Товар", "Описание товара", 50.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product._Product__price == 50.0
    assert product.quantity == 10


def test_create_product_classmethod():
    product = Product.create_product("Товар", "Описание товара", 50.0, 10)
    assert isinstance(product, Product)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product._Product__price == 50.0
    assert product.quantity == 10


def test_price_property():
    product = Product("Товар", "Описание товара", 50.0, 10)
    assert product.price == 50.0


def test_set_price_valid():
    product = Product("Товар", "Описание товара", 50.0, 10)
    with patch("builtins.input", return_value="y"):  # Имитируем ввод пользователя 'y'
        product.price = 40.0
    assert product.price == 40.0


def test_set_price_invalid():
    product = Product("Товар", "Описание товара", 50.0, 10)
    with patch("builtins.input", return_value="n"):  # Имитируем ввод пользователя 'n'
        product.price = 40.0
    assert product.price == 50.0


if __name__ == "__main__":
    pytest.main()