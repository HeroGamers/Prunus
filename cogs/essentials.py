import asyncio
import discord
from discord import Embed
from discord.ext import commands
import os

class essentials(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
        @bot.command()
        @commands.has_permissions(administrator=True)
        async def loadcog(ctx, arg1):
            """Loads a cog"""
            try:
                bot.load_extension(f"cogs.{arg1}")
                await ctx.send(f"Successfully loaded the {arg1} extension")
                channel = bot.get_channel(int(os.getenv('botlog')))
                await channel.send("**[Info]** Admin `%s` loaded the extension %s" % (ctx.author.name, arg1))
            except Exception as e:
                await ctx.send(f"Failed to load the extension {arg1}")
                channel = bot.get_channel(int(os.getenv('botlog')))
                await channel.send(f"**[ERROR]** Failed to load the extension {arg1} - {e}")

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def listcogs(ctx):
            """Lists all the cogs"""
            embed = discord.Embed(title="Cogs", color=discord.Color.green(),
                description="`essentials, info, moderation, administration, fun`")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def unloadcog(ctx, arg1):
            """Unloads a cog"""
            if arg1 == 'essentials':
                await ctx.send(f"**[ERROR]** Please do not try to unload the {arg1} extension")
            else:
                try:
                    bot.unload_extension(f"cogs.{arg1}")
                    await ctx.send(f"Successfully unloaded the {arg1} extension")
                    channel = bot.get_channel(int(os.getenv('botlog')))
                    await channel.send("**[Info]** Moderator `%s` unloaded the extension %s" % (ctx.author.name, arg1))
                except Exception as e:
                    await ctx.send(f"Failed to unload the extension {arg1}")
                    channel = bot.get_channel(int(os.getenv('botlog')))
                    await channel.send(f"**[ERROR]** Failed to unload the extension {arg1} - {e}")
            
def setup(bot):
    bot.add_cog(essentials(bot))
