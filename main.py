import discord
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("https://twitter.com"):
      #await message.channel.send("hello")
        
        newMessage = message.content.replace("https://twitter.com","https://fxtwitter.com")
        await message.channel.send(newMessage)
    

keep_alive()
client.run('ODY5MzE2NjIzNjI0OTgyNTI4.YP8cMg.W1_P0AJBnY7Doi-DVUWpjd5fz2o')
