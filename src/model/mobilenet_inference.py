# - MobileNetV2: Pretrained CNN model
# - preprocess_input: Normalizes image pixel values as expected by this model
# - decode_predictions: Converts raw model outputs into human-readable labels
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
# Utility module for loading and converting images
from tensorflow.keras.preprocessing import image

# Load the MobileNetV2 model with pretrained weights from ImageNet
model = MobileNetV2(weights="imagenet")

def predict_dish(img_path):

    # Load and resize image to 224x224 pixels (required input size for MobileNetV2)
    img = image.load_img(img_path, target_size=(224, 224))

    # Convert the image to a numpy array tensor suitable for model input (224, 224, 3)
    img_array = image.img_to_array(img)

    # Add batch dimension to the image array (1, 224, 224, 3) since model expects batches of images
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess image to match the input format expected by MobileNetV2 (scales pixel values to [-1, 1])
    img_array = preprocess_input(img_array)

    # Run prediction representing the model's confidence in each of the 1000 ImageNet classes
    predictions = model.predict(img_array)

    # Decode predictions (top 1) to get the most likely dish name and its confidence score
    decoded = decode_predictions(predictions, top=1)[0][0] 

    dish_name = decoded[1] # Get the predicted dish name (second element of the tuple)
    confidence = float(decoded[2])
    return dish_name, confidence