from fastapi import FastAPI
from pydantic import BaseModel
import grpc
import time
from chatMessage_pb2_grpc import ChatServerStub
from chatMessage_pb2 import ChatRequest
from pydantic import BaseModel

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"


class ChatRequestApi(BaseModel):
    id: int
    message: str
    user: str

channel = grpc.insecure_channel("localhost:50052")
stub = ChatServerStub(channel)


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Got model alexnet"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "Got model lenet"}
    else:
        return {"model_name": "", "message": "Invalid model.."}

@app.post("/chats/create")
async def create_chat_message(chatRequest: ChatRequestApi):
    start_time = time.time()
    print("Doing grpc create request....")
    request = ChatRequest(id=chatRequest.id, message=chatRequest.message, user=chatRequest.user)
    result = stub.Create(request)
    if result:
        print(f"GRPC Request finished in time:: {time.time() - start_time}")
        return {"message": f"Chat Message created"}
    else:
        return {"message:" f"Request failed"}

