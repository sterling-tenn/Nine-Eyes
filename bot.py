import discord
from discord.ext import commands

from config import COMMAND_PREFIX, BOT_TOKEN

client = commands.Bot(command_prefix = COMMAND_PREFIX)
extensions = ["voice_commands","utilities","misc"]

@client.event
async def on_ready():
    print("Logged in as {0.user}, bot is ready.".format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await client.process_commands(message)

if __name__ == "__main__":
    for extension in extensions:
        client.load_extension(extension)
        print(f"Loaded extension: {extension}")
    client.run(BOT_TOKEN)