[1mdiff --git a/.gitignore b/.gitignore[m
[1mnew file mode 100644[m
[1mindex 0000000..2eea525[m
[1m--- /dev/null[m
[1m+++ b/.gitignore[m
[36m@@ -0,0 +1 @@[m
[32m+[m[32m.env[m
\ No newline at end of file[m
[1mdiff --git a/Configuration.py b/Configuration.py[m
[1mnew file mode 100644[m
[1mindex 0000000..5f93b03[m
[1m--- /dev/null[m
[1m+++ b/Configuration.py[m
[36m@@ -0,0 +1,20 @@[m
[32m+[m[32mimport os[m
[32m+[m[32mfrom dotenv import load_dotenv[m
[32m+[m
[32m+[m
[32m+[m[32mclass Configuration:[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        load_dotenv()[m
[32m+[m[32m        self.DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")[m
[32m+[m[32m        self.GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")[m
[32m+[m[32m        self.GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")[m
[32m+[m[41m        [m
[32m+[m
[32m+[m[32m    def getBotToken(self):[m
[32m+[m[32m        return self.DISCORD_BOT_TOKEN[m
[32m+[m
[32m+[m[32m    def getGoogleSearchApiKey(self):[m
[32m+[m[32m        return self.GOOGLE_SEARCH_API_KEY[m
[32m+[m
[32m+[m[32m    def getGoogleSearchEngineId(self):[m
[32m+[m[32m        return self.GOOGLE_SEARCH_ENGINE_ID[m
\ No newline at end of file[m
[1mdiff --git a/Database.py b/Database.py[m
[1mnew file mode 100644[m
[1mindex 0000000..56f6a26[m
[1m--- /dev/null[m
[1m+++ b/Database.py[m
[36m@@ -0,0 +1,9 @@[m
[32m+[m[32mclass SQL:[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        pass[m
[32m+[m[41m    [m
[32m+[m[32m    def getData(self, query):[m
[32m+[m[32m        return [][m
[32m+[m[41m    [m
[32m+[m[32m    def pushData(self, data):[m
[32m+[m[32m        pass[m
\ No newline at end of file[m
[1mdiff --git a/Google.py b/Google.py[m
[1mnew file mode 100644[m
[1mindex 0000000..3685511[m
[1m--- /dev/null[m
[1m+++ b/Google.py[m
[36m@@ -0,0 +1,23 @@[m
[32m+[m[32mfrom googleapiclient.discovery import build[m
[32m+[m[32mimport pprint[m
[32m+[m
[32m+[m[32mclass Google:[m
[32m+[m[32m    def __init__(self, searchApiKey, searchEngineId):[m
[32m+[m[32m        self.searchApiKey = searchApiKey[m
[32m+[m[32m        self.searchEngineId = searchEngineId[m
[32m+[m
[32m+[m[32m    def search(self, query):[m
[32m+[m[32m        print("Search query:", query)[m
[32m+[m[32m        service = build("customsearch", "v1", developerKey=self.searchApiKey)[m
[32m+[m
[32m+[m[32m        result = service.cse().list(q=query, cx=self.searchEngineId).execute()[m
[32m+[m[32m        # print("Query Result:", result)[m
[32m+[m
[32m+[m[32m        top_result = [][m
[32m+[m[32m        if "items" in result.keys():[m
[32m+[m[32m            for each in result["items"]:[m
[32m+[m[32m                # print(each)[m
[32m+[m[32m                top_result.append(each["link"])[m
[32m+[m[32m                if len(top_result) == 5:[m
[32m+[m[32m                    break[m
[32m+[m[32m        return top_result[m
[1mdiff --git a/__pycache__/Configuration.cpython-37.pyc b/__pycache__/Configuration.cpython-37.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..57a6971[m
Binary files /dev/null and b/__pycache__/Configuration.cpython-37.pyc differ
[1mdiff --git a/__pycache__/Configuration.cpython-38.pyc b/__pycache__/Configuration.cpython-38.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..fc94159[m
Binary files /dev/null and b/__pycache__/Configuration.cpython-38.pyc differ
[1mdiff --git a/__pycache__/Database.cpython-38.pyc b/__pycache__/Database.cpython-38.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..3d3a463[m
Binary files /dev/null and b/__pycache__/Database.cpython-38.pyc differ
[1mdiff --git a/__pycache__/Google.cpython-38.pyc b/__pycache__/Google.cpython-38.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..5d3b9ef[m
Binary files /dev/null and b/__pycache__/Google.cpython-38.pyc differ
[1mdiff --git a/main.py b/main.py[m
[1mindex 1aea5c7..d2c0ebf 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,4 +1,11 @@[m
 import discord[m
[32m+[m[32mimport Configuration[m
[32m+[m[32mimport Google[m
[32m+[m[32mimport Database[m
[32m+[m
[32m+[m[32mconfig = Configuration.Configuration()[m
[32m+[m[32mgoogle = Google.Google(config.getGoogleSearchApiKey(), config.getGoogleSearchEngineId())[m
[32m+[m[32mdb = Database.SQL()[m
 [m
 class MyClient(discord.Client):[m
     async def on_ready(self):[m
[36m@@ -6,12 +13,31 @@[m [mclass MyClient(discord.Client):[m
 [m
     async def on_message(self, message):[m
         print(message.channel, message.author, message.author.name, message.content)[m
[32m+[m[41m        [m
         if message.author == self.user:[m
             return [m
 [m
[31m-        if message.content == 'ping':[m
[31m-            await message.channel.send('pong')[m
[32m+[m[32m        if message.content.startswith("hi"):[m
[32m+[m[32m            await message.channel.send('hey')[m
[32m+[m
[32m+[m[32m        if message.content.startswith("!google"):[m
[32m+[m[32m            query = message.content.split(" ", 1)[m
[32m+[m[32m            response = "Empty query!"[m
[32m+[m[32m            if(len(query) >= 2):[m
[32m+[m[32m                response = '\n'.join(google.search(query[1]))[m
[32m+[m[32m                db.pushData(query[1])[m
[32m+[m[32m            await message.channel.send(response)[m
 [m
[31m-client = MyClient()[m
[31m-client.run('Njk3MTE5NTQ2NzY2Nzg2NjEw.XoypXg.l8PDKKsqeaK_uVmPnomRn5psNVE')[m
 [m
[32m+[m[32m        if message.content.startswith("!recent"):[m
[32m+[m[32m            query = message.content.split(" ", 1)[m
[32m+[m[32m            response = "Empty query!"[m
[32m+[m[32m            if(len(query) >= 2):[m
[32m+[m[32m                response = '\n'.join(db.getData(query[1]))[m
[32m+[m[32m            await message.channel.send(response)[m
[32m+[m
[32m+[m[32m        await message.channel.send('Wrong query!\nPlease try again.')[m
[32m+[m
[32m+[m[32mclient = MyClient()[m
[32m+[m[32mprint("Bot Started")[m
[32m+[m[32mclient.run(config.getBotToken())[m
