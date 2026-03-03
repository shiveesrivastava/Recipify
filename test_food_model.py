from src.model.food101_inference import predict_dish_pytorch

dish, confidence = predict_dish_pytorch("test_images/test6.jpg")
print(dish, confidence)