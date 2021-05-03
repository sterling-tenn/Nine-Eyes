import discord
from discord.ext import commands

class VoiceCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        # If the user calls the command while not in a voice channel
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()

    @commands.command()
    async def leave(self,ctx):
        # If the bot is not in a voice channel
        if not ctx.voice_client:
            await ctx.send("Not in a voice channel.")
        else:
            await ctx.guild.voice_client.disconnect()
            
    @commands.command()
    async def play(self,ctx):
        await join(ctx)

def setup(client):
    client.add_cog(VoiceCommands(client))