from fastapi import FastAPI

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"
app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Got model alexnet"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "Got model lenet"}
    else:
        return {"model_name": "", "message": "Invalid model.."}