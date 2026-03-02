from utils.recipe_loader import load_recipes

def compute_similarity(predicted_ingredients, recipe_ingredients):
    # Computes a similarity score based on ingredient overlap
    predicted_set = set(predicted_ingredients)
    recipe_set = set(recipe_ingredients)

    overlap = predicted_set.intersection(recipe_set)

    score = len(overlap) / len(recipe_set)

    return score


def recommend_recipe(predicted_ingredients, dish_type):
    # Returns the single best matching recipe with full details.
    recipes = load_recipes()
    best_recipe = None
    best_score = 0

    for recipe_name, recipe_data in recipes.items():

        if recipe_data["dish_type"] != dish_type:
            continue

        recipe_ingredients = recipe_data["ingredients"]
        score = compute_similarity(predicted_ingredients, recipe_ingredients)

        if score > best_score:
            best_score = score
            best_recipe = {
                "name": recipe_name,
                "ingredients": recipe_ingredients,
                "instructions": recipe_data["instructions"],
                "score": score
            }
    return best_recipe