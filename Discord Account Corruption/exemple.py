import requests, random

token = open("token.txt", "r", encoding="utf-8").readline()

theme = "dark"
langue = "en-US"
guildName = "Hello Skids"
guildColor = random.randint(1337,2022)

Data = {}

r = requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers={"authorization": token}, json=Data)
print(r.text)