from functools import lru_cache

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from messagebird import Client
from pydantic import BaseModel

from config import Settings


@lru_cache()
def get_settings():
    return Settings()


class Sms(BaseModel):
    message: str


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/message")
def post_message(sms: Sms, settings: Settings = Depends(get_settings)):
    client = Client(settings.access_key)
    message = client.message_create(
        settings.originator,
        "+923365859518",
        sms.message,
        {"reference": "Foobar", "type": "flash"},
    )

    print(message)

    return sms
