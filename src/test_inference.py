from model.mobilenet_inference import predict_dish

dish, confidence = predict_dish("../test_images/test2.jpg")

print("Predicted Dish:", dish)
print("Confidence:", round(confidence, 2))