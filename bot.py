import discord
import asyncio
import datetime
from discord.ext import commands
from discord import Embed
from pathlib import Path
import sys, traceback
import os
from Util import logging
import config

bot = commands.Bot(command_prefix=os.getenv('prefix'), description='I guess this is a bot, it does bot things.')

startup_extensions = ["essentials",
                      "info"]

@bot.event
async def on_ready():
    await logging.log("**[Info]** The bot has started!", bot)
    print("\n")
    stream = discord.Streaming(name="Hero's channel on Twitch!", url="https://www.twitch.tv/herogamersdk", twitch_name="herogamersdk")
    await bot.change_presence(activity=stream)

@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send("This command cannot be used in private messages")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=Embed(color=discord.Color.red(), description="I am missing some permission(s)!"))
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=Embed(color=discord.Color.red(), description="You are missing some permission(s)!"))
    elif isinstance(error, commands.CheckFailure):
        return
    elif isinstance(error, commands.CommandOnCooldown):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        return
    elif isinstance(error, commands.BadArgument):
        return
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        await ctx.send("Something went wrong while executing that command... Sorry!")
        await logging.log("**[ERROR]** %s" % error, bot)

@bot.event
async def on_guild_join(guild):
    await logging.log("**[Info]** Joined a new guild (`%s` - `%s`)" % (guild.name, guild.id), bot)

@bot.event
async def on_member_update(before, after):
    for role in before.roles:
        if role.id == 530778945105428501:
            return
    for role in after.roles:
        if role.id == 530778945105428501:
            emojis = bot.emojis
            for emoji in emojis:
                if emoji.id == 561907145231171625:
                    emote = "<:" + emoji.name + ":" + str(emoji.id) + ">"
                    break
                emote = u"\U0001F4E5"
            
            channel = bot.get_channel(221998962247204864)

            embed = discord.Embed(title="Welcome to Treeland, " + after.display_name, color=discord.Color.from_rgb(255, 105, 180), timestamp=datetime.datetime.utcnow(),
                description=emote + " <@" + str(after.id) + "> just became a member of Treeland! Please welcome them!")
            embed.set_footer(text="New Member of Treeland", icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
            embed.set_thumbnail(url=after.avatar_url)
            await channel.send(embed=embed)
            await logging.log("**[Info]** A member just got the rising role... %s#%s" % (after.name, after.discriminator), bot)

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    ctx:commands.Context = await bot.get_context(message)
    if message.content.startswith(os.getenv('prefix')):
        if ctx.command is not None:
            await logging.log("**[Command]** `%s` (%s) used the `%s` command in the guild `%s` (%s), in the channel `%s` (%s)" % (ctx.author.name, ctx.author.id, ctx.invoked_with, ctx.guild.name, ctx.guild.id, ctx.channel.name, ctx.channel.id), bot)
            await bot.invoke(ctx)
    else:
        return

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            logging.logDebug(f"[ERROR] Failed to load extension {extension}. - {e}")

bot.run(os.getenv('token'))
