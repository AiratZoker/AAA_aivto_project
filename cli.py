"""
CLI-приложение для заказа и доставки пиццы.

Создано с использованием библиотеки Click.

Команды:
    - menu: Выводит меню доступных пицц.
    - order: Готовит и доставляет выбранную пиццу.

Примеры использования:
    $ python -m cli menu
    $ python -m cli order pepperoni --delivery

"""
import click
from typing import List, Dict, Optional
import random


class Pizza:
    """Представляет общую пиццу с указанием размера,
    названия и ингредиентов."""

    def __init__(
            self,
            size: Optional[str] = None,
            pizza: Optional[str] = None
    ) -> None:
        """
        Инициализирует объект Pizza.

        Параметры:
        - size (str): Размер пиццы (например, "L", "XL").
        - pizza (str): Название пиццы.

        Возвращает:
        None
        """
        self.size: Optional[str] = size
        self.ingredients: List[str] = []
        self.pizza: Optional[str] = pizza

    def add_ingredient(self, ingredient: str) -> None:
        """
        Добавляет ингредиент к пицце.

        Параметры:
        - ingredient (str): Ингредиент для добавления.

        Возвращает:
        None
        """
        self.ingredients.append(ingredient)

    def add_name_pizza(self, name: str) -> None:
        """
        Устанавливает название пиццы.

        Параметры:
        - name (str): Название пиццы.

        Возвращает:
        None
        """
        self.pizza = name

    def dict(self) -> Dict[str, Optional[str]]:
        """
        Возвращает словарь, представляющий пиццу.

        Возвращает:
        dict: Словарь с деталями пиццы.
        """
        return {
            "pizza": self.pizza,
            "size": self.size,
            "ingredients": self.ingredients

        }


class Margherita(Pizza):
    """Представляет пиццу Маргарита, подкласс Pizza."""

    def __init__(self, size: str, pizza: str) -> None:
        """
        Инициализирует пиццу Маргарита.

        Параметры:
        - size (str): Размер пиццы (например, "L", "XL").
        - pizza (str): Название пиццы.

        Возвращает:
        None
        """
        super().__init__(size)
        self.add_name_pizza(pizza)
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella")
        self.add_ingredient("tomatoes")


class Pepperoni(Pizza):
    """Представляет Пепперони-пиццу, подкласс Pizza."""

    def __init__(self, size: str, pizza: str) -> None:
        """
        Инициализирует Пепперони-пиццу.

        Параметры:
        - size (str): Размер пиццы (например, "L", "XL").
        - pizza (str): Название пиццы.

        Возвращает:
        None
        """
        super().__init__(size)
        self.add_name_pizza(pizza)
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella")
        self.add_ingredient("pepperoni")


class Hawaiian(Pizza):
    """Представляет Гавайскую пиццу, подкласс Pizza."""

    def __init__(self, size: str, pizza: str) -> None:
        """
        Инициализирует Гавайскую пиццу.

        Параметры:
        - size (str): Размер пиццы (например, "L", "XL").
        - pizza (str): Название пиццы.

        Возвращает:
        None
        """
        super().__init__(size)
        self.add_name_pizza(pizza)
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella")
        self.add_ingredient("chicken")
        self.add_ingredient("pineapples")


def log(func):
    """
    Декоратор для логирования времени выполнения функции.

    Параметры:
    - func (callable): Функция, для которой будет выполняться логирование.

    Возвращает:
    callable: Обернутая функция с логированием времени выполнения.
    """

    def wrapper(*args, **kwargs):
        """
        Обертка функции с логированием времени выполнения.

        Параметры:
        - *args: Позиционные аргументы для функции.
        - **kwargs: Именованные аргументы для функции.

        Возвращает:
        В зависимости от функции, которая была обернута.
        """
        minutes = random.randint(1, 5)
        print(f"{func.__name__} - {minutes} минут!")

        result = func(minutes, *args, **kwargs)
        return result

    return wrapper


@click.group()
def cli():
    """Выберите пиццу из меню"""
    pass


@cli.command()
def menu():
    """
    Выводит меню доступных пицц.

    Возвращает:
    None
    """
    margherita = Margherita(size=None, pizza="Margherita").dict()
    pepperoni = Pepperoni(size=None, pizza="Pepperoni").dict()
    hawaiian = Hawaiian(size=None, pizza="Hawaiian").dict()

    click.echo(f"{margherita['pizza']}: "
               f"{', '.join(margherita['ingredients'])}"
               )
    click.echo(f"{pepperoni['pizza']}: "
               f"{', '.join(pepperoni['ingredients'])}"
               )
    click.echo(f"{hawaiian['pizza']}: "
               f"{', '.join(hawaiian['ingredients'])}"
               )


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Обрабатывает заказ пиццы, с возможностью доставки.

    Параметры:
    - pizza (str): Название пиццы для заказа.
    - delivery (bool): Включать ли доставку.

    Возвращает:
    None
    """
    bake(pizza)

    if delivery:
        deliverys()
    else:
        pickup()


@log
def bake(minutes: int, pizza: str) -> None:
    """
    Готовит пиццу.

    Параметры:
    - minutes (int): Время готовки в минутах.
    - pizza (str): Название пиццы для приготовления.

    Возвращает:
    None
    """
    if pizza == "pepperoni":
        print(f"Пепперони готова за {minutes} минуту!")
    elif pizza == "margherita":
        print(f"Маргарита готова за {minutes} минуты!")
    elif pizza == "hawaiian":
        print(f"Гавайская готова за {minutes} минуты!")


@log
def deliverys(minutes: int) -> None:
    """
    Доставляет пиццу.

    Параметры:
    - minutes (int): Время доставки в минутах.

    Возвращает:
    None
    """
    print(f"Доставили пиццу за {minutes} минут!")


@log
def pickup(minutes: int) -> None:
    """
    Самовывоз.

    Параметры:
    - minutes (int): Время самовывоза в минутах.

    Возвращает:
    None
    """
    print(f"Самовывоз за {minutes} минут")


if __name__ == '__main__':
    cli()
