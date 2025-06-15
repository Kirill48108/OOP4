import pytest
from src.class_product import Product

@pytest.fixture
def product_apple():
    return Product("Apple", "red", 99.9, 1000)


def test_init_product(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.description == "red"
    assert product_apple.price == 99.9
    assert product_apple.quantity == 1000