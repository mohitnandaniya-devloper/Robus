import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")
    MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", 500))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

    @staticmethod
    def validate():
        if Config.DISCORD_TOKEN is None:
            raise ValueError("DISCORD_TOKEN_KEY is not set in the .env file")
        
        if Config.GEMINI_API_KEY is None:
            raise ValueError("GEMINI_API_KEY is not set in the .env file")
        
        if Config.GEMINI_MODEL is None:
            raise ValueError("GEMINI_MODEL is not set in the .env file")
        
        if not isinstance(Config.MAX_OUTPUT_TOKENS, int):
            raise ValueError("MAX_OUTPUT_TOKENS must be an integer")
        
        if not isinstance(Config.TEMPERATURE, float):
            raise ValueError("TEMPERATURE must be a float")
        
Config.validate()
