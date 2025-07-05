import pytest


def test_smartphone_product_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_product_init1(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone_product_init2(smartphone3):
    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


def test_smartphone_product_error(smartphone1, smartphone2, smartphone3):
    with pytest.raises(TypeError):
        result = smartphone1 + 1
