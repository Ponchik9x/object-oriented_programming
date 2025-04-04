class Product:
    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        cost_of_products_1 = self.quantity * self.__price
        cost_of_products_2 = other.quantity * other.__price

        return cost_of_products_1 + cost_of_products_2

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value <= self.__price:
                answer = input(f"Заменить стоимость на: {value} (y/n)\n").lower()
                if answer == "y":
                    self.__price = value

    @classmethod
    def new_product(cls, param: dict):
        name = param["name"]
        description = param["description"]
        __price = param["price"]
        quantity = param["quantity"]
        return cls(name, description, __price, quantity)


class Category:
    name: str
    description: str
    products: list

    category_count: list[str] = []
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """"""
        self.name = name
        self.description = description
        self.__products = products

        self.category_count += [name]
        self.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count}"

    def add_product(self, value: list | Product):
        self.__products.append(value)
        self.product_count += 1

    @property
    def products(self):
        return self.__products

    # @property
    # def get_quantity(self):
    #     return f" {Product.name}, {Product.price} руб. Остаток: {Product.quantity} шт."

    @products.getter
    def products(self):
        result = []
        for i in self.__products:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(result)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
