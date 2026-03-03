import sys
from src.pipeline import run_pipeline

def main():

    if len(sys.argv) < 2:
        print("Usage: python src/main.py <image_path>")
        return

    image_path = sys.argv[1]

    result = run_pipeline(image_path)

    if "error" in result:
        print(f"\nError: {result['error']}")
        if "confidence" in result:
            print(f"Confidence: {round(result['confidence'], 2)}")
        return

    print(f"\nPredicted Dish: {result['dish']}")
    print(f"Confidence: {round(result['confidence'], 2)}")

    print("\nIngredients:")
    for item in result["ingredients"]:
        print(f"- {item}")

    print(f"\nRecommended Recipe: {result['recipe']['name']}")
    print(f"Match Score: {round(result['recipe']['match_score'], 2)}")

    print("\nInstructions:")
    for step in result["recipe"]["instructions"]:
        print(f"- {step}")

if __name__ == "__main__":
    main()