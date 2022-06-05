from functools import lru_cache

from fastapi import Depends, FastAPI
from messagebird import Client
from pydantic import BaseModel

from config import Settings


@lru_cache()
def get_settings():
    return Settings()


class Sms(BaseModel):
    message: str


app = FastAPI()


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
