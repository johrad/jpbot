import json

with open('config.json', 'r') as file:
    data = file.read()

foo = json.loads(data)

bot_token = str(foo["token"])
bot_prefix = str(foo["prefix"])
#print(bot_prefix + bot_token)
