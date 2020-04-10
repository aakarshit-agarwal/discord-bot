import os
import urllib.parse as urlparse
from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()
        self.__DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN'] or os.getenv("DISCORD_BOT_TOKEN")
        self.__GOOGLE_SEARCH_API_KEY = os.environ['GOOGLE_SEARCH_API_KEY'] or os.getenv("GOOGLE_SEARCH_API_KEY")
        self.__GOOGLE_SEARCH_ENGINE_ID = os.environ['GOOGLE_SEARCH_ENGINE_ID'] or os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        self.__DATABASE_URL = os.environ['DATABASE_URL'] or os.getenv("DATABASE_URL")
        self.__LOGGING_LEVEL = os.environ['LOGGING_LEVEL'] or os.getenv("LOGGING_LEVEL")

    def getBotToken(self):
        return self.__DISCORD_BOT_TOKEN

    def getGoogleConfig(self):
        return {
            "API_KEY" : self.__GOOGLE_SEARCH_API_KEY,
            "ENGINE_ID" : self.__GOOGLE_SEARCH_ENGINE_ID
        }

    def getDatabaseConfig(self):
        url = urlparse.urlparse(self.__DATABASE_URL)
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        return {
            "USER" : user,
            "PASSWORD" : password,
            "HOST" : host,
            "NAME" : dbname,
            "PORT" : port
        }
    
    def getLoggingLevel(self):
        return self.__LOGGING_LEVEL
