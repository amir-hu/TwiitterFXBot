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
      try:
        embeds = message.embeds
        print(embeds[0].to_dict()['description'])
        if(embeds[0].to_dict()['description']=="Failed to scan your link!"):
          await message.delete()
      except:
        pass


    if message.content.lower().startswith("cp"):
      
      data = message.content.split(" ")
      newMessage = "enter in format cp <pokemon name> <iv> <filters>"
      if(len(data) >= 3):
        newMessage = "p!m s --n " + data[1] + " --iv >" + data[2] + " --o price+ "
        for x in range(3,len(data)):
          newMessage = newMessage + "--" + data[x] + " "
      await  message.channel.send(newMessage)
      
    if message.content.startswith("https://twitter.com"):
      
        
        newMessage = message.content.replace("https://twitter.com","https://fxtwitter.com")
        embeds = await message.channel.send(newMessage)
        
    

keep_alive()
client.run(os.getenv(('TOKEN')))
