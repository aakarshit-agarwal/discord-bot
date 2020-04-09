import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(message.channel, message.author, message.author.name, message.content)
        if message.author == self.user:
            await message.channel.send('Hey You')

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('Njk3MTE5NTQ2NzY2Nzg2NjEw.XoypXg.l8PDKKsqeaK_uVmPnomRn5psNVE')