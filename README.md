# Созданы два класса Category и Product

### В классе Product определены следующие свойства и методы:

1. Название (name)
2. Описание (description)
3. Цена (price)
4. Количество в наличии (quantity)

Аргумент "price" определен как приватный

В класс Добавлены методы:

price (getter для приватного свойства price)
price (setter с проверкой ввода положительного значения и с уточнения у пользователя о его намерении изменить данные)
new_product (classmethod, позволяет добавлять новый продукт, который передается через словарь)

### В классе Category определены следующие свойства и методы:

1. Название (name)
2. Описание (description)
3. Список товаров категории (products)

Аргумент "products" определен как приватный

Для класса Category добавлены два атрибута класса. 
Доступ к этим атрибутам у каждого объекта класса, и в них хранится общая информация для всех объектов. 
Эти атрибуты хранят в себе количество категорий и количество товаров.

Атрибуты класса заполняются автоматически при инициализации нового объекта.


В класс Добавлены методы:

add_product (метод для добавления в приватный атрибут products новых объектов класса Product)
products (getter который возвращает приватный атрибут products)
products (setter который возвращает данные в формате: 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')



# Тесты 

### Тесты из модуля main для классов, которые проверяют:

1. корректность инициализации объектов класса Category
2. корректность инициализации объектов класса Product
3. подсчет количества продуктов,
4. подсчет количества категорий.
