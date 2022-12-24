from fastapi import APIRouter
from ..request_model import Data
from ..models.predict import SmartphonePricePredict
router = APIRouter()
@router.get("/")
async def check_healthy():
    return {200: "OK"}


@router.post(
    "/predict/",
    description="Evaluate smartphone's price",
)
async def predict(data: Data):

    predictor = SmartphonePricePredict(model_name="DecisionTree")
    result = predictor.predict(data)
    return result