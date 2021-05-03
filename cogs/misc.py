import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def owo(self,ctx):
        await ctx.message.channel.send("uwu")

def setup(client):
    client.add_cog(Misc(client))