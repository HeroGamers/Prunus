import asyncio
import discord
from discord import Embed
from discord.ext import commands
import os

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        @bot.command()
        async def helpme(ctx):
            """Get help"""
            await ctx.send("No help to get here, but [click here](https://gist.github.com/HeroGamers/a92b824d899981c4c6c287978a54548c) for the Privacy Policy! :)")

def setup(bot):
    bot.add_cog(Info(bot))
