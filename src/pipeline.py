from src.config import MODEL_TYPE, CONFIDENCE_THRESHOLD
from src.utils.ingredient_mapper import get_ingredients
from src.utils.recommendation_engine import recommend_recipe
from src.utils.label_mapper import normalize_label

# Dynamic model import
if MODEL_TYPE == "tensorflow":
    from src.model.mobilenet_inference import predict_dish as predict_model
elif MODEL_TYPE == "pytorch":
    from src.model.food101_inference import predict_dish_pytorch as predict_model
else:
    raise ValueError("Invalid MODEL_TYPE in config.py")


def run_pipeline(image_path):
    # Core AI Pipeline. Returns a structured response with dish, confidence, ingredients, and recipe details.
    dish, confidence = predict_model(image_path)

    dish = normalize_label(dish)

    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "error": "Low confidence prediction",
            "confidence": confidence
        }

    ingredients = get_ingredients(dish)

    if ingredients is None:
        return {
            "error": "Dish not supported",
            "dish": dish,
            "confidence": confidence
        }

    recipe = recommend_recipe(
        predicted_ingredients=ingredients,
        dish_type=dish
    )

    if recipe is None:
        return {
            "error": "Recipe not found",
            "dish": dish,
            "confidence": confidence
        }

    return {
        "dish": dish,
        "confidence": confidence,
        "ingredients": ingredients,
        "recipe": {
            "name": recipe["name"],
            "instructions": recipe["instructions"],
            "match_score": recipe["score"]
        }
    }