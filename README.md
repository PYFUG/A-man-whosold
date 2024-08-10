import discord
from discord.ext import commands
import os
import random

files = os.listdir('images')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def mem(ctx):
    random_file = random.choice(files)
    with open(f'images/{random_file}', 'rb') as f:


        picture = discord.File(f)

    await ctx.send(file=picture)

files2 = os.listdir('images2')

@bot.command()
async def c(ctx):
    random_file = random.choice(files2)
    with open(f'images2/{random_file}', 'rb') as f:


        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run('')
