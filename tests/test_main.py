import pytest

from main import Category, Product


@pytest.fixture
def product_1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_1(product_1: Product) -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_1],
    )


def test_class_init_product(product_1: Product) -> None:
    """тест на правильность работы инициализации класса"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_class_init_category(category_1: Category, product_1: Product) -> None:
    """тест на правильность работы инициализации класса"""
    assert category_1.name == "Телевизоры"
    assert (
        category_1.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_1.products == [product_1]

    assert category_1.category_count == ["Телевизоры"]
    assert category_1.product_count == len(category_1.products)
