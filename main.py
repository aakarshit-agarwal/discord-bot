import discord
import Logger
import logging
import Configuration
import Database
import Google

logger = logging.getLogger()
config = Configuration.Configuration()
google = Google.Google()
db = Database.SQL()

class MyClient(discord.Client):
    async def on_ready(self):
        logger.info('\nLogged on as %s', self.user)

    async def on_message(self, message):
        logger.debug("\nChannel: %s \nAuthor: %s \nAuthor Name:%s \nMessage:%s",\
             message.channel, message.author, message.author.name, message.content)
        
        if message.author == self.user:
            return 

        elif message.content.startswith("hi"):
            await message.channel.send('hey')

        elif message.content.startswith("!google"):
            query = message.content.split(" ", 1)
            response = ""
            if(len(query) >= 2):
                searchResult = google.search(query[1])
                logger.debug('\nGoogle Search result %s', searchResult)
                for i, each in enumerate(searchResult):
                    response += "\n" + str(i + 1) + '. ' + each["title"] + "\n" + each["link"] + "\n"
                db.pushData(message.author.name, query[1])
            else:
                response = "Empty query!"
            await message.channel.send("\nResult:" + response)

        elif message.content.startswith("!recent"):
            query = message.content.split(" ", 1)
            response = ""
            if(len(query) >= 2):
                recentResult = db.getData(message.author.name, query[1])
                logger.debug('\nRecent Search result %s', recentResult)
                for i, each in enumerate(recentResult):
                    response += "\n" + str(i + 1) + '. ' + each
            else:
                response = "Empty query!"
            await message.channel.send("\nRecent Quries:" + response)

client = MyClient()
logger.info('\nBot Started')
client.run(config.getBotToken())
