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

    @commands.command(aliases = ["purge","delete"])
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount:int):
        try:
            await ctx.channel.purge(limit = amount + 1)
            await ctx.send(f"{amount} message(s) have been deleted.",delete_after = 5)
        except discord.Forbidden:
            await ctx.send("I don't have the 'Manage Messages' permission.")
        except discord.MissingPermissions:
            await ctx.send("You are missing 'Manage Messages' permission to run this command.")

def setup(client):
    client.add_cog(Utilities(client))