import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self,client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_message_delete(self,message):
    #     author = message.author
    #     content = message.content

    #     await message.channel.send(f"{author} deleted a message:\n{content}")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount:int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f"{amount} message(s) have been deleted.",delete_after = 5)

def setup(client):
    client.add_cog(Utilities(client))