import discord
from discord.ext import commands

from config import BOT_TOKEN

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await client.process_commands(message)

@client.command()
async def owo(ctx):
    await ctx.message.channel.send("uwu")

client.run(BOT_TOKEN)