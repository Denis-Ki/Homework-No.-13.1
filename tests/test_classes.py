import pytest
from src.classes import Category, Product, Smartphone, LawnGrass
from unittest.mock import patch


@pytest.fixture
def empty_category():
    return Category("Категория", "Описание")


@pytest.fixture
def sample_product():
    return Product.create_product("Товар", "Описание товара", 50.0, 10)


@pytest.fixture
def smartphone_product():
    return Smartphone("Смартфон", "Описание товара", 60.0, 20, "синий", 100, "A120", "128 Mb")


@pytest.fixture
def lawn_grass_product():
    return LawnGrass("Трава", "Описание травы", 1.0, 10, "зеленая", "Голландия", "10 дней")


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


def test_product_init(sample_product):
    assert sample_product.name == "Товар"
    assert sample_product.description == "Описание товара"
    assert sample_product._Product__price == 50.0
    assert sample_product.quantity == 10


def test_create_product_classmethod():
    product = Product.create_product("Товар", "Описание товара", 50.0, 10)
    assert isinstance(product, Product)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product._Product__price == 50.0
    assert product.quantity == 10


def test_price_property(sample_product):
    assert sample_product.price == 50.0


def test_set_price_valid(sample_product):
    with patch("builtins.input", return_value="y"):  # Имитируем ввод пользователя 'y'
        sample_product.price = 40.0
    assert sample_product.price == 40.0


def test_set_price_invalid(sample_product):
    with patch("builtins.input", return_value="n"):  # Имитируем ввод пользователя 'n'
        sample_product.price = 40.0
    assert sample_product.price == 50.0


def test_str_product(sample_product):
    assert str(sample_product) == "Товар, 50.0 руб. Остаток: 10 шт."


def test_str_category(empty_category):
    product1 = Product.create_product("Товар 1", "Описание товара 1", 50.0, 20)
    product2 = Product.create_product("Товар 2", "Описание товара 2", 80.0, 15)
    empty_category.add_product(product1)
    empty_category.add_product(product2)
    assert str(empty_category) == "Категория, количество продуктов: 2 шт."


def test__add__product():
    product1 = Product.create_product("Товар 1", "Описание товара 1", 50.0, 20)
    product2 = Product.create_product("Товар 2", "Описание товара 2", 80.0, 15)
    assert product1 + product2 == 50.0 * 20 + 80.0 * 15


def test_smartphone_init(smartphone_product):
    assert smartphone_product.name == "Смартфон"
    assert smartphone_product.description == "Описание товара"
    assert smartphone_product._Product__price == 60.0
    assert smartphone_product.quantity == 20
    assert smartphone_product.color == "синий"
    assert smartphone_product.performance == 100
    assert smartphone_product.model == "A120"
    assert smartphone_product.memory == "128 Mb"


def test_lawn_grass_init(lawn_grass_product):
    assert lawn_grass_product.name == "Трава"
    assert lawn_grass_product.description == "Описание травы"
    assert lawn_grass_product._Product__price == 1.0
    assert lawn_grass_product.quantity == 10
    assert lawn_grass_product.color == "зеленая"
    assert lawn_grass_product.country == "Голландия"
    assert lawn_grass_product.period == "10 дней"


if __name__ == "__main__":
    pytest.main()