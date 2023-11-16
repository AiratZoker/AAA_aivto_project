import pytest
from click.testing import CliRunner
from cli import cli
from cli import Pizza, Margherita, Pepperoni, Hawaiian

runner = CliRunner()


def test_menu_command_all():
    result = runner.invoke(cli, ['menu'])

    assert result.exit_code == 0
    assert "Margherita" in result.output
    assert "Pepperoni" in result.output
    assert "Hawaiian" in result.output


def test_order_command_pepperoni_del():
    result = runner.invoke(cli, ['order', 'pepperoni', '--delivery'])

    assert result.exit_code == 0
    assert "Пепперони готова" in result.output
    assert "Доставили пиццу" in result.output


def test_order_command_margherita_del():
    result = runner.invoke(cli, ['order', 'margherita', '--delivery'])

    assert result.exit_code == 0
    assert "Маргарита готова" in result.output
    assert "Доставили пиццу" in result.output


def test_order_command_hawaiian_del():
    result = runner.invoke(cli, ['order', 'hawaiian', '--delivery'])

    assert result.exit_code == 0
    assert "Гавайская готова" in result.output
    assert "Доставили пиццу" in result.output


def test_order_command_pepperoni_out_del():
    result = runner.invoke(cli, ['order', 'pepperoni'])

    assert result.exit_code == 0
    assert "Пепперони готова" in result.output
    assert "Самовывоз" in result.output


def test_order_command_margherita_out_del():
    result = runner.invoke(cli, ['order', 'margherita'])

    assert result.exit_code == 0
    assert "Маргарита готова" in result.output
    assert "Самовывоз" in result.output


def test_order_command_hawaiian_out_del():
    result = runner.invoke(cli, ['order', 'hawaiian'])

    assert result.exit_code == 0
    assert "Гавайская готова" in result.output
    assert "Самовывоз" in result.output


def test_pizza_class():
    pizza = Pizza(size="L", pizza="Custom Pizza")
    pizza.add_ingredient("tomato sauce")
    pizza.add_ingredient("mozzarella")
    pizza.add_name_pizza("Custom Pizza")

    assert pizza.size == "L"
    assert pizza.pizza == "Custom Pizza"
    assert pizza.ingredients == ["tomato sauce", "mozzarella"]


def test_margherita_class():
    margherita = Margherita(size="L", pizza="Margherita")

    assert margherita.size == "L"
    assert margherita.pizza == "Margherita"
    assert margherita.ingredients == ["tomato sauce", "mozzarella", "tomatoes"]


def test_pepperoni_class():
    pepperoni = Pepperoni(size="XL", pizza="Pepperoni")

    assert pepperoni.size == "XL"
    assert pepperoni.pizza == "Pepperoni"
    assert pepperoni.ingredients == ["tomato sauce", "mozzarella", "pepperoni"]


def test_hawaiian_class():
    hawaiian = Hawaiian(size="L", pizza="Hawaiian")

    assert hawaiian.size == "L"
    assert hawaiian.pizza == "Hawaiian"
    assert hawaiian.ingredients == ["tomato sauce", "mozzarella", "chicken", "pineapples"]
