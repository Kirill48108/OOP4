import pytest
from src.class_category import Category
@pytest.fixture
def category_fruit():
    return Category("fruits", "fruits from India", ["banana", "mango"])


def test_init_category(category_fruit):
    assert category_fruit.name == "fruits"
    assert category_fruit.description == "fruits from India"
    assert category_fruit.products == ["banana", "mango"]
    assert category_fruit.product_count == 2
    assert Category.category_count == 1