import asyncio
import discord
from discord.ext import commands
import os


class usercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # @bot.command()
        # async def getflair(ctx):
        #    """Gets a flair on the Reddit dependent on your role on Treeland"""
        #    ctx.author.


def setup(bot):
    bot.add_cog(usercommands(bot))
