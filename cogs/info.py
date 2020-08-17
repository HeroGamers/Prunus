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
            await ctx.send("No help to get here, but DM Hero if you want the Privacy Policy! :)")

def setup(bot):
    bot.add_cog(Info(bot))
