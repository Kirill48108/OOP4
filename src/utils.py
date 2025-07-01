import json
import os

from src.class_category import Category
from src.class_product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF=8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    products = []
    for product in data:
        categories = []
        for category in product["category_list"]:
            categories.append(Category(**category))
        product["category_list"] = categories
        products.append(Product(**product))
    return products


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    products_data = create_objects_from_json(raw_data)
    print(products_data[0].name)
    print(products_data[0].category_list)
