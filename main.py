import json
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response


#  To start the server do 
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload  
app = FastAPI()

@dataclass
class Channel:
    id: str
    name: str
    tags:list[str] = field(default_factory=list)
    description: str = ""

channels: dict[str,Channel] = {}

with open('channels.json') as f:
    channels_raw = json.load(f)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel

@app.get("/")
def read_root() -> Response:
    return Response('The server is running !')

@app.get("/channel/{channel_id}", response_model=Channel)
def read_item(channel_id:str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(status = 404, detail = "Channel not found")
    return channels[channel_id]
