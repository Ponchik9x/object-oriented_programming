from main import Product


def test_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
