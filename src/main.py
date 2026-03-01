from model.mobilenet_inference import predict_dish
from utils.ingredient_mapper import get_ingredients
import os
import sys

CONFIDENCE_THRESHOLD = 0.60


def main():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return
    image_path = sys.argv[1]

    dish, confidence = predict_dish(image_path)

    print(f"\nPredicted Dish: {dish}")
    print(f"Confidence: {round(confidence, 2)}")

    if confidence < CONFIDENCE_THRESHOLD:
        print("\nPrediction confidence too low. Please try a clearer image.")
        return

    ingredients = get_ingredients(dish)

    if ingredients is None:
        print("\nDetected object is not a supported food item.")
        return

    print("\nIngredients:")
    for item in ingredients:
        print(f"- {item}")


if __name__ == "__main__":
    main()