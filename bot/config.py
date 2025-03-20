import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN_KEY")

    @staticmethod
    def validate():
        if Config.DISCORD_TOKEN is None:
            raise ValueError("DISCORD_TOKEN_KEY is not set in the .env file")

Config.validate()
