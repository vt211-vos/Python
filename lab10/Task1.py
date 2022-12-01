import pytest
from shop import Shop

shop = Shop('АТБ', 'продуктовий')
def test_describe_shop():
    assert shop.describe_shop() == "Name=>АТБ  Type=>продуктовий"
def test_open_shop():
    assert shop.open_shop() == "АТБ is open"
def test_set_number_of_units():
    shop.set_number_of_units(4)
    assert shop.number_of_units == 4
def test_increment_number_of_units():
    shop.increment_number_of_units()
    assert shop.number_of_units == 5