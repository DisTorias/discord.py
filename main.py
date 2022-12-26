import discord.py
from discord.ext import commands

bot = commadns.Bot(command_prefix="s!', intents = intents = discord.Intents().all())

@bot.event
async def on_ready():
    print("Бот Активировался!")
