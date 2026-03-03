from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from src.pipeline import run_pipeline
import shutil
import os

app = FastAPI(title="Recipify API")
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    
    # Accepts an image file and returns predicted dish and recipe.
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = run_pipeline(file_path)

    # Delete temp file after processing
    os.remove(file_path)

    if "error" in result:
        return JSONResponse(status_code=400, content=result)

    return result