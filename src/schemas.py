from pydantic import BaseModel
from typing import List, Optional

class RecipeResponse(BaseModel):
    name: str
    instructions: List[str]
    match_score: float

class PredictionResponse(BaseModel):
    dish: str
    confidence: float
    ingredients: List[str]
    recipe: Optional[RecipeResponse]

class ErrorResponse(BaseModel):
    error: str
    message: str