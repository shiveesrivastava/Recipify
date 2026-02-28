import json
import os

# Load JSON once
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "ingredients.json")

# INGREDIENT_DATA is a dictionary loaded from the JSON file with same structure as the JSON content
with open(DATA_PATH, "r") as f:
    INGREDIENT_DATA = json.load(f)

def get_ingredients(dish_name):
    dish_name = dish_name.lower()

    # Handle exact match first (base case)
    if dish_name in INGREDIENT_DATA:
        return INGREDIENT_DATA[dish_name]["base"]

    # Handle variant format like cheese_pizza
    if "_" in dish_name:
        parts = dish_name.split("_")
        modifier = parts[0]
        base = parts[-1]

        if base in INGREDIENT_DATA:
            base_ingredients = INGREDIENT_DATA[base]["base"]

            if modifier in INGREDIENT_DATA[base]["variants"]:
                variant_ingredients = INGREDIENT_DATA[base]["variants"][modifier]
                return base_ingredients + variant_ingredients

            return base_ingredients
    return None