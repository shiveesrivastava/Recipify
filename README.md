Recipify 
AI-powered recipe assistant using image recognition.

Recipify takes an image of food, predicts the dish using a pretrained deep learning model and maps it to structured ingredient data.

Features:
1. Image classification using MobileNetV2 (ImageNet pretrained)
2. Confidence threshold filtering
3. Food-only domain restriction
4. Structured ingredient knowledge base (JSON-based)
5. CLI-based interaction
6. Modular architecture for scalability

Pipeline:
Image
  ↓
MobileNetV2 (Image Classification)
  ↓
Confidence Threshold Check
  ↓
Food Filter (Supported Dishes Only)
  ↓
Ingredient Mapping (Structured JSON)
  ↓
Ingredient Output

This architecture separates:
ML perception layer
Knowledge layer
Reasoning layer
Execution layer

Structure:
Recipify/
│
├── src/
│   ├── model/
│   │   └── mobilenet_inference.py
│   ├── utils/
│   │   └── ingredient_mapper.py
│   └── main.py
│
├── data/
│   └── ingredients.json
│
├── test_images/
├── requirements.txt
└── README.md

How to Run:
1. Activate Virtual Environment: .\venv\Scripts\Activate.ps1
2. Run: python src/main.py test_images/your_image.jpg