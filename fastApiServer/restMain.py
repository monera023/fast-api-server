from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequestApi(BaseModel):
    id: int
    message: str
    user: str

app = FastAPI()

@app.post("/chats/create")
async def create_chat(request: ChatRequestApi) -> bool:
    print(f"Got request in rest call {request.dict()}")
    return True