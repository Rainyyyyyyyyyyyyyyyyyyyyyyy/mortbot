import discord
import requests
import json
import os
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '$')
bot.remove_command('help')
token = 'ODkyNDUzODE2NTQzMzc1NDQw.YVNIYg.__QGPijlnrHqD_KzWY2N6PpBq5s'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="for $help"))
    print("Bot started")

extensions = ['cogs.CommandsEvents', 'cogs.HelpsCommands', 'cogs.PriceCommand']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(token)