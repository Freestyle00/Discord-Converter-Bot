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
    if regex.search("[mMoOrRnNiNgG]$" ,message) is not None:
        response = "Good morning to you too"
    await message.channel.send(response)
client.run(TOKEN)