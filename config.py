from pydantic import BaseSettings


class Settings(BaseSettings):
    access_key: str
    originator: str

    class Config:
        env_file = ".env"
