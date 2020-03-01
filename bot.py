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
                      "info",
                      "Tasks"]


# For checking the welcome channel
async def welcome_channel():
    # Defining bot messages for the welcome channel
    welcomeembeds = []
    # --- Welcome image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://styles.redditmedia.com/t5_22a6oh/styles/bannerBackgroundImage_gfuciyxjzod31.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Welcome message ---
    embed = discord.Embed(title="Welcome to Treeland", color=discord.Color.from_rgb(255, 105, 180),
                          description="Hi, and welcome to Treeland! :blesswave:\n\n"
                                      
                                      "You can see Treeland as your new home, away from home. A second family. "
                                      "We want to keep a civil tone in here, whilst still having heck loads of fun.\n\n"
                                      
                                      "If you need help with anything, go ahead and ping an active @Staff, "
                                      "but please only ping if you find it necessary, "
                                      "or else you might get your ass whooped.\n"
                                      "If you think something should be added, removed, changed or whatever, "
                                      "please send it into a Staff's DM's, in a clean and clear way :meowokhand:\n\n"
                                      
                                      "We don't want to bore someone to death with a huge list of rules, so here are "
                                      "a few, and we expect all of you to follow them :blessfingergunsamusedreverse:")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Rules image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://styles.redditmedia.com/t5_22a6oh/styles/bannerBackgroundImage_gfuciyxjzod31.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Rules message ---
    embed = discord.Embed(title="The Rules of Treeland", color=discord.Color.from_rgb(255, 105, 180),
                          description="*So... You want to hear a story, eh? One about treasure hunters? "
                                      "Haha, have I got a story for you!*\n"
                                      "Wait, wrong Transcript... Well, to become a fully-fledged Treelander you've got "
                                      "to know your way around our rules, but fret not! They are quite simple:\n\n"

                                      # Rule 1
                                      "**1.** Behave properly to others.\n"
                                      # Rule 2
                                      "**2.** No NSFW content in channels that aren't marked as NSFW. "
                                      "Explicit pornographic content isn't allowed anywhere in Treeland.\n"
                                      # Rule 3
                                      "**3.** Don't break the Discord Terms of Service.\n"
                                      # Rule 4
                                      "**4.** Stick to the Discord Community Guidelines "
                                      "(as well as the Discord Partnership Code of Conduct).\n")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Roles image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://styles.redditmedia.com/t5_22a6oh/styles/bannerBackgroundImage_gfuciyxjzod31.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Roles message ---
    embed = discord.Embed(title="The Roles of Treeland", color=discord.Color.from_rgb(255, 105, 180),
                          description="Now... What are those shiny Roles I see in the side panel?\n"
                                      "Well... allow me to explain\n\n"

                                      "**:green_heart: 🢡 Treelander of the Day:** A random member of Treeland chosen "
                                      "every day at 12 PM (CET). Gets access to write in #totd-chat.\n "
                                      "\n"
                                      "**:purple_heart: 🢡 Royalty of Treeland:** These people are true followers of "
                                      "Treeland, and have been for many many years.\n "
                                      "**:blue_heart: 🢡 Epic Gamers:** People in this role are either freakin' "
                                      "awesome and are a part of our staff team <3\n "
                                      "**:seedling: 🢡 Master Tree Grower:** :NitroBoost: This role is given to "
                                      "people who are very good at growing our trees here in Treeland, by boosting "
                                      "our small land with their Nitro Boost :NitroBoost:\n "
                                      "\n"
                                      "**:evergreen_tree: 🢡 Evergreen:** To go even further beyond. This individual "
                                      "is either to be feared or looked down upon, as they clearly have given their "
                                      "souls away and dedicated themselves to Treeland. Reached at a whoppin' 50000 "
                                      "Server Exp.\n "
                                      "**:tanabata_tree: 🢡 Tanabata:** Wowie, now we're gettin' there. If an "
                                      "individual has this role, you should know that they know their shit. Reached "
                                      "at 10000 Server Exp.\n "
                                      "**:palm_tree: 🢡 Palm:** An individual who has this role should know what's "
                                      "happening around here by now. Reached at Level 5000 Server Exp.\n "
                                      "**:deciduous_tree: 🢡 Treelander:** This role is given to people who have "
                                      "reached 500 Server Exp, and those people are now a fully fledged citizen of "
                                      "Treeland.\n "
                                      "**:smiling_face_with_3_hearts: 🢡 Peeps:** This role is given to people who "
                                      "joined at the Invite-only stage of the Heroji Emote Servers.\n "
                                      "**:earth_africa: 🢡 IRL:** This role is given to people who I know and have "
                                      "met physically. "
                                      "**:balloon: 🢡 Risings:** You might be familiar with this role, well it's the "
                                      "role you got when you first got here. It's the role for people that are on "
                                      "their way up the rankings.\n")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
    welcomeembeds.append(embed)


    # Editing the current bot messages, if they aren't identical with the ones defined above
    channel = bot.get_channel(221996778092888065)  # channel is #welcome

    current_botmessages = []
    async for message in channel.history(limit=20):
        if message.author == bot.user:
            current_botmessages.append(message)





@bot.event
async def on_ready():
    # Bot startup is now done...
    logging.logDebug("----------[LOGIN SUCESSFULL]----------", "INFO")
    logging.logDebug("     Username: " + bot.user.name, "INFO")
    logging.logDebug("     UserID:   " + str(bot.user.id), "INFO")
    logging.logDebug("--------------------------------------", "INFO")
    print("\n")

    logging.logDebug("Checking the welcome channel!", "INFO")
    await welcome_channel()
    logging.logDebug("Done checking the welcome channel!", "INFO")
    print("\n")

    await logging.log("The bot is ready!", bot, "INFO")
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
        await logging.log(error, bot, "ERROR")

@bot.event
async def on_guild_join(guild):
    await logging.log("Joined a new guild (`%s` - `%s`)" % (guild.name, guild.id), bot, "INFO")

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
            await logging.log("A member just got the rising role... %s#%s" % (after.name, after.discriminator), bot, "INFO")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    ctx:commands.Context = await bot.get_context(message)
    if message.content.startswith(os.getenv('prefix')):
        if ctx.command is not None:
            await logging.log("`%s` (%s) used the `%s` command in the guild `%s` (%s), in the channel `%s` (%s)" % (ctx.author.name, ctx.author.id, ctx.invoked_with, ctx.guild.name, ctx.guild.id, ctx.channel.name, ctx.channel.id), bot, "INFO")
            await bot.invoke(ctx)
    else:
        return

if __name__ == '__main__':
    # we setup the logger first
    logging.setup_logger()
    # load extensions
    for extension in startup_extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            logging.log(f"Failed to load extension {extension}. - {e}", bot, "ERROR")

bot.run(os.getenv('token'))
