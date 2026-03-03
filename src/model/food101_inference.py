import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

# Load model globally so it loads ONLY ONCE
MODEL_NAME = "nateraw/food"

processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)

model.eval()


def predict_dish_pytorch(image_path):
    # Predict dish using Food-101 Vision Transformer model.
    """    
    Returns:
        dish_name (str)
        confidence (float)
    """
    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=1)

    confidence, predicted_class_idx = torch.max(probabilities, dim=1)

    dish_name = model.config.id2label[predicted_class_idx.item()]

    return dish_name, confidence.item()