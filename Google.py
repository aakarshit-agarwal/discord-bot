import Configuration
import logging
from googleapiclient.discovery import build

config = Configuration.Configuration()
logger = logging.getLogger()

class Google:
    def __init__(self):
        googleConfig = config.getGoogleConfig()
        self.__searchApiKey = googleConfig["API_KEY"]
        self.__searchEngineId = googleConfig["ENGINE_ID"]

    def search(self, query):
        logger.debug("Search query: %s", query)
        service = build("customsearch", "v1", developerKey=self.__searchApiKey)

        result = service.cse().list(q=query, cx=self.__searchEngineId).execute()
        logger.debug("Query Result:%s ", result)

        top_result = []
        if "items" in result.keys():
            for each in result["items"]:
                top_result.append({
                    "title": each["title"],
                    "link": each["link"]
                })
                if len(top_result) == 5:
                    break
        return top_result
