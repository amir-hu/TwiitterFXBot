import os
import discord
from replit import db
from keep_alive import keep_alive
from modelbuild import getpred

client = discord.Client()
id = "716390085896962058"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):



#"""    if message.author.id == 716390085896962058:
#      try:
#        imagelink = message.embeds[0].image.url
#        prediction = getpred(imagelink)
#        print("after prediction")
#        await message.channel.send(prediction)
#      except:
#        pass 

    
    if message.content.lower().startswith("cm"):
      newMessage = f"<@{id}> m s --mine --o price-"
      await message.channel.send(newMessage)

    if message.content.lower().startswith("cl "):
      
      
      data = message.content.split(" ")
      newMessage = "enter in format cp <pokemon name> <iv> <filters>"
      if(len(data) >= 3):
        newMessage = f"<@{id}> m s --n " + data[1] + " --level >" + data[2] + " --o price+ "
        for x in range(3,len(data)):
          newMessage = newMessage + "--" + data[x] + " "
      await  message.channel.send(newMessage)
      


    if message.content.lower().startswith("poo"):
        mess = message.content.split(" ")
        prediction = getpred(mess[1])
        await message.channel.send(prediction)
      

    if message.content.lower().startswith("fxhelp"):
      embed = discord.Embed(Title="Commands", 
      description="All the commands for this bot " )
      embed.add_field(name="mps <Amir | Hassan | Barre | View >", value="mario party standing ", inline=False) 
      embed.add_field(name="bc <Died | Alive | View >", value="the ratio of times that has failed us and crashed on us ", inline=False) 
      embed.add_field(name="cp <Pokemon Name> <IV Percentage> <filters>", value="check price on poketwo based on iv", inline=False)
      embed.add_field(name="cl <Pokemon Name> <level > <filters>", value="check price on poketwo based on level", inline=False)
      embed.add_field(name="cm", value="check what you have on the market ordered by price", inline=False)  
      await message.channel.send(embed=embed)
    mpStandings = {
      "amir":0,
      "hassan":0,
      "barre":0,
      "view":0
    }

    if message.content.lower().startswith("mps "):
      f = open("mpScores.txt","r")
      data = f.read().split(":")
      f.close()
      if "amir" in db.keys():
        mpStandings["amir"] = int(db["amir"])
        mpStandings["hassan"] = int(db["hassan"])
        mpStandings["barre"] = int(db["barre"])
      else:
        mpStandings["amir"] = 0
        mpStandings["hassan"] = 0
        mpStandings["barre"] = 0
      content = message.content.lower().split(" ")
      mpStandings[content[1]] = mpStandings[content[1]] + 1
      sorted(mpStandings.items(), key=lambda x: x[1])
      embed=discord.Embed(title="Mario Party Standings ", 
      description="This is the current standings for mario party wins: ", color=0xFF5733)
      embed.add_field(name="Barres wins", value=mpStandings["barre"])
      embed.add_field(name="Amir wins", value=mpStandings["amir"])
      embed.add_field(name="Hassan wins", value=mpStandings["hassan"])
      embed.set_thumbnail(url="https://www.pinclipart.com/picdir/big/456-4561725_super-mario-star-png-mario-party-star-png.png")

      
      await message.channel.send(embed=embed)

      f = open("mpScores.txt","w")
      newStandings = "%s:%s:%s"%(mpStandings["amir"],mpStandings["hassan"],mpStandings["barre"])
      db["amir"] = mpStandings["amir"]
      db["hassan"] = mpStandings["hassan"]
      db["barre"] = mpStandings["barre"]
      f.write(newStandings)
      f.close()


    if message.content.lower().startswith("bc"):
      f = open("Barre.txt", "r")
      data = f.read().split(":")
      f.close()
      alive = int(data[0])
      dead = int(data[1])
      content = message.content.lower().split(" ")
      if(content[1]=="died"):
        dead = dead + 1
      if(content[1]=="alive"):
        alive = alive + 1

      result = alive - dead
      reaction = "No ones suprised really"
      if(result>0):
        reaction = " MY GOD YOU NEVER THOUGHT YOU WOULD SEE THE DAY "
      newMessage = "Current ratio of barre ghosting to pulling an undertaker is: " + str(dead) + " to " + str(alive) + " which puts us at a grand total of " +  str(result) + " " + reaction 
      embed=discord.Embed(title="Barre Crashing to Undertakering", 
      description=str(dead)+":"+str(alive), color=0xFF5733)
      embed.add_field(name="Grand total", value=str(result) + " " + reaction)
      
      
      await message.channel.send(embed=embed)
      f = open("Barre.txt", "w")
      f.write(str(alive) + ":" + str(dead))
      f.close()
      

    if message.content.lower().startswith("cp "):
      
      
      data = message.content.split(" ")
      newMessage = "enter in format cp <pokemon name> <iv> <filters>"
      if(len(data) >= 3):
        newMessage = f"<@{id}> m s --n " + data[1] + " --iv >" + data[2] + " --o price+ "
        for x in range(3,len(data)):
          newMessage = newMessage + "--" + data[x] + " "
      await  message.channel.send(newMessage)
      
    if message.content.startswith("https://twitter.com"):
        newMessage = message.content.replace("https://twitter.com","https://vxtwitter.com")
        embeds = await message.channel.send(newMessage)
    

keep_alive()
try:
  client.run(os.getenv(('TOKEN')))
except:
  os.system("kill 1")

