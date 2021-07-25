from dis import dis
import Converter
import os
import discord
import re as regex
from dotenv import load_dotenv
Con = Converter.Converting()
load_dotenv()
TOKEN = os.getenv("DISCORD-BOT-TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = ""
    if regex.search("(?i)Morning" ,str(message.content)) is not None:
        response = "Good morning to you too"
    if regex.findall("([0-9]+)[ °]*[fF]" ,str(message.content)) != []:
        response =  str(Con.TemperatureFtoC(int(regex.findall("([0-9]+)[ °]*[fF]" ,str(message.content))[0])))
    if response  ==  "" or []:
        return
    await message.channel.send(response)
client.run(TOKEN)