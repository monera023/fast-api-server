from fastapi import FastAPI
from pydantic import BaseModel
import grpc
import time
import requests
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

@app.post("/chats/grpc/create")
async def create_chat_message(chatRequest: ChatRequestApi):
    start_time = time.time()
    print("Doing grpc create request....")
    request = ChatRequest(id=chatRequest.id, message=chatRequest.message, user=chatRequest.user)
    result = stub.Create(request)
    if result:
        print(f"GRPC Request finished in time:: {(time.time() - start_time) * 1000}")
        return {"message": f"Chat Message created"}
    else:
        return {"message:" f"Request failed"}


@app.post("/chats/rest/create")
async def create_chat_message_rest(chatRequest: ChatRequestApi):
    start_time = time.time()
    print("Doing rest create request...")
    url = "http://localhost:8081/chats/create"
    response = requests.post(url, json=chatRequest.dict())
    print(f"Response.. {response}")
    if response:
        print(f"Rest Request finished in time:: {(time.time() - start_time) * 1000}")
        return {"message": "Got success"}
        
