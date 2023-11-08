import discord
from discord.ext import commands
from bot_mantik import *
from BotA_ayarlar import *

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
async def hello(ctx):
    await ctx.send(f'Hi {bot.user}! I am a chatbot!')

@bot.command()
async def password(ctx, passs: int):
    await ctx.send(gen_pass(passs))

@bot.command()
async def bye(ctx):
    await ctx.send(":slight_smile:")

@bot.command()
async def cool(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

bot.run(ayarlar["TOKEN"])
