import discord
import Configuration
import Google
import Database

config = Configuration.Configuration()
google = Google.Google(config.getGoogleSearchApiKey(), config.getGoogleSearchEngineId())
db = Database.SQL()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(message.channel, message.author, message.author.name, message.content)
        
        if message.author == self.user:
            return 

        if message.content.startswith("hi"):
            await message.channel.send('hey')

        if message.content.startswith("!google"):
            query = message.content.split(" ", 1)
            response = "Empty query!"
            if(len(query) >= 2):
                response = '\n'.join(google.search(query[1]))
                db.pushData(query[1])
            await message.channel.send(response)


        if message.content.startswith("!recent"):
            query = message.content.split(" ", 1)
            response = "Empty query!"
            if(len(query) >= 2):
                response = '\n'.join(db.getData(query[1]))
            await message.channel.send(response)

        await message.channel.send('Wrong query!\nPlease try again.')

client = MyClient()
print("Bot Started")
client.run(config.getBotToken())
