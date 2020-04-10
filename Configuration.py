import os
from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()
        self.__DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        self.__GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.__GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        self.__DATABASE_USER = os.getenv("DATABASE_USER")
        self.__DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        self.__DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.__DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.__DATABASE_PORT = os.getenv("DATABASE_PORT")
        self.__LOGGING_LEVEL = os.getenv("LOGGING_LEVEL")

    def getBotToken(self):
        return self.__DISCORD_BOT_TOKEN

    def getGoogleConfig(self):
        return {
            "API_KEY" : self.__GOOGLE_SEARCH_API_KEY,
            "ENGINE_ID" : self.__GOOGLE_SEARCH_ENGINE_ID
        }

    def getDatabaseConfig(self):
        return {
            "USER" : self.__DATABASE_USER,
            "PASSWORD" : self.__DATABASE_PASSWORD,
            "HOST" : self.__DATABASE_HOST,
            "NAME" : self.__DATABASE_NAME,
            "PORT" : self.__DATABASE_PORT
        }
    
    def getLoggingLevel(self):
        return self.__LOGGING_LEVEL
