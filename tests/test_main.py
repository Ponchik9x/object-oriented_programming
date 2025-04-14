import pytest

from main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product1() -> Product:
    """Fixture телефон samsung"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_tv(product1: Product) -> Category:
    """Fixture категория телевизоры"""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product1],
    )


@pytest.fixture
def product_smartphone1() -> Smartphone:
    """Fixture смартфон1 Iphone"""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_smartphone2() -> Smartphone:
    """Fixture смартфон2 Samsung"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_grass1() -> LawnGrass:
    """Fixture газонная трава"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_tv():
    """Fixture телевизор"""
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category_smartphones1(product_smartphone1):
    """Fixture категория смарфоны"""
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [product_smartphone1])


@pytest.fixture
def user_value():
    """Fixture значение пользователя: 800"""
    return 800


@pytest.fixture
def new_product() -> Product:
    """Fixture данные продукта в словаре. Смартфон samsung"""
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture
def cls_new_product():
    """Fixture данные продукт в словаре. Смартфон Samsung"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


def test_class_init_product(product1: Product) -> None:
    """тест на правильность работы инициализации класса"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_class_init_category(category_tv: Category, product1: Product) -> None:
    """тест на правильность работы инициализации класса"""
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert category_tv.products == "Телевизоры, количество продуктов: 5 шт."
    assert category_tv.category_count == ["Телевизоры"]
    assert category_tv.product_count == 1


def test_price(new_product: Product):
    """тест на правильность работы метода new_product, price, из класса Product"""
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_change_price_valid_answer_y(new_product: Product, monkeypatch):
    """Тест на правильность работы ввода (ответ: 'y')
    и работу метода price из класса Product с положительным значением(замена на: '800')"""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    new_product.price = 800
    assert new_product.price == 800


def test_change_price_valid_answer_n(new_product: Product, monkeypatch):
    """Тест на правильность работы ввода (ответ: 'n') и работу метода price с положительным значением
    из класса Product"""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    new_product.price = 800
    assert new_product.price == 180000.0


def test_change_price_zero(new_product: Product, monkeypatch):
    """Тест на правильность работы работу метода price с нулевым значением (ввод: '0')"""
    new_product.price = 0
    assert new_product.price == 180000.0


def test_change_price_below_zero(new_product: Product, monkeypatch):
    """Тест на правильность работы метода price с отрицательным значением (ввод: '-800')
    из класса Product"""
    new_product.price = -800
    assert new_product.price == 180000


def test_new_product(cls_new_product: dict):
    """Тест на правильность метода new_product из класса Product"""
    new_product_test = Product.new_product(cls_new_product)
    assert new_product_test.name == "Samsung Galaxy S23 Ultra"
    assert new_product_test.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_test.price == 180000.0
    assert new_product_test.quantity == 5


def test_add_product(category_smartphones1, product_grass1, product_smartphone2):
    """Тест на правильность добавления продукта в категорию"""
    category_smartphones1.add_product(product_smartphone2)
    assert category_smartphones1.products == "Смартфоны, количество продуктов: 13 шт."
    assert category_smartphones1.category_count == ["Телевизоры", "Смартфоны"]
    assert category_smartphones1.product_count == 2
    with pytest.raises(TypeError):
        category_smartphones1.add_product("Not a product")


def test_add_prod(product_smartphone1, product_smartphone2, product_grass1, capsys):
    """Тест на правильность работы функции сложения двух продуктов"""

    valid_sum = product_smartphone1 + product_smartphone2
    assert valid_sum == 2580000.0

    with pytest.raises(TypeError):
        product_smartphone1 + product_grass1


def test_for_class_product__str__(product_smartphone1: Product):
    assert str(product_smartphone1) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_for_class_product__add__(product_smartphone1, product_smartphone2):
    add_prod = product_smartphone1 + product_smartphone2
    assert add_prod == 2580000.0


def test_for_class_category__str__(category_smartphones1):
    assert str(category_smartphones1) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_class_smartphone():
    """тест на правильность работы класса Smartphone"""
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_class_lawngrass():
    """Тест на правильность работы класса LawnGrass"""
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    assert grass2.name == "Газонная трава 2"
    assert grass2.description == "Выносливая трава"
    assert grass2.price == 450.0
    assert grass2.quantity == 15
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"
    assert grass2.color == "Темно-зеленый"


def test_init_new_product_invalid():
    """Тест на ошибку ValueError при попытке добавить продукт с нулевым количеством"""
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price_valid(product_smartphone1, product_smartphone2):
    """Тест на положительный ответ метода вычисления средней стоимости товаров в категории (метод: middle_price)"""
    category1 = Category("Смартфоны", "Категория смартфонов", [product_smartphone1, product_smartphone2])
    assert category1.middle_price()


def test_middle_price_invalid():
    """Тест на возбуждение ошибки метода middle_price"""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    sum_prod = category_empty.middle_price()
    assert sum_prod == 0
