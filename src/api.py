from fastapi import FastAPI, UploadFile, File
from fastapi import HTTPException
from src.pipeline import run_pipeline
from src.schemas import PredictionResponse
from src.config import logger
import shutil
import os

app = FastAPI(title="Recipify API")
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "recipify-api"
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    
    # Accepts an image file and returns predicted dish and recipe.
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    logger.info(f"Image uploaded: {file.filename}")

    # Save uploaded file temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = run_pipeline(file_path)
    logger.info(f"Pipeline result: {result}")

    # Delete temp file after processing
    os.remove(file_path)

    if "error" in result:
        error_message = result["error"]
        logger.error(f"Prediction error: {error_message}")

        if error_message == "Dish not supported":
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "UNSUPPORTED_DISH",
                    "message": error_message
                }
            )

        if error_message == "Recipe not found":
            raise HTTPException(
                status_code=404,
                detail={
                    "error": "RECIPE_NOT_FOUND",
                    "message": error_message
                }
            )

        raise HTTPException(
            status_code=400,
            detail={
                "error": "PREDICTION_ERROR",
                "message": error_message
            }
        )

    logger.info(f"Prediction success: {result['dish']} ({result['confidence']:.2f})")
    return result