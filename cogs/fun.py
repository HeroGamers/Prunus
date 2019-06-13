import asyncio
import discord
from discord import Embed
from discord.ext import commands
import os

class Fun:
    def __init__(self,bot):
        self.bot = bot

        @bot.command()
        async def spoilmychars(ctx, *args):
            """Spoilertags everything"""
            message = args
            print(message)
            await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
            for i in range( len(message) ):
                await ctx.send("||%s||" % message[i])
            await ctx.send("```{}```")

def setup(bot):
    bot.add_cog(Fun(bot))
