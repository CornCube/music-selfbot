from os import path
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=False)


@bot.event
async def on_ready():
    print('-' * 20)
    print('Logged in as')
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-' * 20)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

if path.isfile("token.txt"):
    with open("token.txt") as f:
        token = f.readline()
    print("[INFO] Starting up and logging in...")
    bot.run(token)
else:
    print("Please enter your discord account token:")
    token = input()
    print("[INFO] Saving token...")
    with open("token.txt", "w") as f:
        f.write(token)
    print("[INFO] Starting up and logging in...")
    bot.run(token)
