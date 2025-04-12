from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self):
        """Вывод строки с названием продукта, стоимостью в рублях и остаток продукта."""
        pass

    @abstractmethod
    def __add__(self, *args, **kwargs):
        """Сложение общей стоимости на остатке одного товара с общей стоимостью на остатке второго товара"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Возвращает значение цены продукта(приватный аргумент)"""
        pass

    @price.getter
    @abstractmethod
    def price(self):
        """Проверяет стоимость на положительное значение.
        Запрашивает у пользователя ввод на замену стоимости товара если новая стоимость меньше текущей."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Добавление нового продукта из словаря."""
