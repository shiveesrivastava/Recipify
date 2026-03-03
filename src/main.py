from utils.ingredient_mapper import get_ingredients
from utils.recommendation_engine import recommend_recipe
from config import MODEL_TYPE, CONFIDENCE_THRESHOLD
import sys

# Dynamic model selection
if MODEL_TYPE == "tensorflow":
    from model.mobilenet_inference import predict_dish as predict_model
elif MODEL_TYPE == "pytorch":
    from model.food101_inference import predict_dish_pytorch as predict_model
else:
    raise ValueError("Invalid MODEL_TYPE in config.py")


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <image_path>")
        return
    image_path = sys.argv[1]

    # Perception Layer
    dish, confidence = predict_model(image_path)
    from utils.label_mapper import normalize_label
    dish = normalize_label(dish)

    print(f"\nPredicted Dish: {dish}")
    print(f"Confidence: {round(confidence, 2)}")

    # Confidence Filter
    if confidence < CONFIDENCE_THRESHOLD:
        print("\nPrediction confidence too low. Please try a clearer image.")
        return

    # Knowledge Layer
    ingredients = get_ingredients(dish)

    if ingredients is None:
        print("\nDetected dish is not currently supported in ingredients database.")
        return

    print("\nIngredients:")
    for item in ingredients:
        print(f"- {item}")

    # Recommendation Layer
    recipe = recommend_recipe(
        predicted_ingredients=ingredients,
        dish_type=dish
    )

    if recipe is None:
        print("\nNo recipe found.")
        return

    print(f"\nRecommended Recipe: {recipe['name']}")
    print(f"Match Score: {round(recipe['score'], 2)}")

    print("\nInstructions:")
    for step in recipe["instructions"]:
        print(f"- {step}")


if __name__ == "__main__":
    main()