import os
from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()
        self.DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        self.GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        self.DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")

    def getBotToken(self):
        return self.DISCORD_BOT_TOKEN

    def getGoogleConfig(self):
        return {
            "API_KEY" : self.GOOGLE_SEARCH_API_KEY,
            "ENGINE_ID" : self.GOOGLE_SEARCH_ENGINE_ID
        }

    def getDatabaseConfig(self):
        return {
            "USER" : self.DATABASE_USER,
            "PASSWORD" : self.DATABASE_PASSWORD,
            "HOST" : self.DATABASE_HOST,
            "NAME" : self.DATABASE_NAME,
        }