import discord
import Configuration
import Google
import Database

config = Configuration.Configuration()

googleConfig = config.getGoogleConfig()
google = Google.Google(googleConfig["API_KEY"], googleConfig["ENGINE_ID"])

db = Database.SQL(config.getDatabaseConfig())

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print("\nRequest:", message.channel, message.author, message.author.name, message.content)
        
        if message.author == self.user:
            return 

        elif message.content.startswith("hi"):
            await message.channel.send('hey')

        elif message.content.startswith("!google"):
            query = message.content.split(" ", 1)
            response = ""
            if(len(query) >= 2):
                searchResult = google.search(query[1])
                for i, each in enumerate(searchResult):
                    response += "\n" + str(i + 1) + '. ' + each["title"] + "\n" + each["link"] + "\n"
                db.pushData(message.author.name, query[1])
            else:
                response = "Empty query!"
            await message.channel.send("Result:\n" + response)

        elif message.content.startswith("!recent"):
            query = message.content.split(" ", 1)
            response = "Empty query!"
            if(len(query) >= 2):
                response = '\n'.join(db.getData(message.author.name, query[1]))
            await message.channel.send("Recent Quries:\n" + response)

client = MyClient()
print("Bot Started")
client.run(config.getBotToken())
