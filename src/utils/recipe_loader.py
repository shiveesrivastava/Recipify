import json
import os

def load_recipes():
    # Loads recipes from data/recipes.json and returns them as a list of dictionaries
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    recipe_path = os.path.join(base_dir, "data", "recipes.json")

    with open(recipe_path, "r") as f:
        recipes = json.load(f)

    return recipes