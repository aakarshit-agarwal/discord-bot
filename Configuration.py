import os
from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()
        self.DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        self.GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        

    def getBotToken(self):
        return self.DISCORD_BOT_TOKEN

    def getGoogleSearchApiKey(self):
        return self.GOOGLE_SEARCH_API_KEY

    def getGoogleSearchEngineId(self):
        return self.GOOGLE_SEARCH_ENGINE_ID