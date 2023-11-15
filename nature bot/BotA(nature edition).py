from re import M
import discord
from discord.ext import commands
from bot_mantik import *
from BotA_ayarlar import *
import os

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def what_to_do(ctx):
    with open("nature bot\recycle1.png", "rb") as a:
        r1=discord.File(a)
    with open("nature bot\recycle2.jpg", "rb") as b:
        r2=discord.File(b)
    with open("nature bot\recycle3.jpg", "rb") as c:
        r3=discord.File(c)
    with open("nature bot\recycle4.jpg", "rb") as d:
        r4=discord.File(d)
    await ctx.send(file=r1, file=r2, file=r3, file=r4)
    await ctx.send("DONT'T EVER THROW AWAY OLD THINGS!")
    await ctx.send("DON'T EVER USE ONE USE THINGS!")

bot.run(ayarlar["TOKEN"])