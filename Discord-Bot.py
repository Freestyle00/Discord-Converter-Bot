from dis import dis

from discord.client import Client
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
    if regex.findall("([-]*[0-9]+)[ °]*[fF]" ,str(message.content)) != []:
        response =  str(Con.TemperatureFtoC(int(regex.findall("([-]*[0-9]+)[ °]*[fF]" ,str(message.content))[0])))
    if regex.findall("([-]*[0-9]+)[ °]*[cC]" ,str(message.content)) != []:
        response =  str(Con.TemperatureCtoF(int(regex.findall("([-]*[0-9]+)[ °]*[cC]" ,str(message.content))[0])))
    if regex.findall("(?i)(-?[0-9]+) *[km]+p?\/? *h+", str(message.content)) != []:
        response = str(Con.SpeedKMHtoMPH(int(regex.findall("(?i)(-?[0-9]+) *[km]+p?\/? *h+", str(message.content))[0])))
    if regex.findall("(?i)(-?[0-9]+) *[mp]+\/? *h+", str(message.content)) != []:
        response = str(Con.SpeedMPHtoKMH(int(regex.findall("(?i)(-?[0-9]+) *[mp]+\/? *h+", str(message.content))[0])))
    measurmentregexvar = regex.findall("(?i)(-?[0-9]+\.?[0-9]?) *(mm|ce|cm|m|km|ki){1}", str(message.content))
    if measurmentregexvar !=[]:
        if Con.MeasurmentWorldtoUS(int(measurmentregexvar[0][0]), measurmentregexvar[0][1]) != False:
            response = Con.MeasurmentWorldtoUS(int(measurmentregexvar[0][0]), measurmentregexvar[0][1])
    measurmentregexvar1 = regex.findall("(?i)(-?[0-9]+\.?[0-9]?) *(mi|ft|fe|yd|ya|in){1}", str(message.content))
    if measurmentregexvar1 != []:
        if Con.MeasurmentUStoWorld(int(measurmentregexvar1[0][0]), measurmentregexvar1[0][1]) != False:
            response = Con.MeasurmentUStoWorld(int(measurmentregexvar1[0][0]), measurmentregexvar1[0][1]) #so apraently findall stores stuff in a tupel and only now it raised an error
    if response  ==  "" or []:
        return
    await message.channel.send(response)

client.run(TOKEN)