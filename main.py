import os
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
      
        
        newMessage = message.content.replace("https://twitter.com","https://fxtwitter.com")
        await message.channel.send(newMessage)
    

keep_alive()
client.run(os.getenv(('TOKEN')))
