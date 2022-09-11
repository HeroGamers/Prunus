import discord
import datetime
from discord.ext import commands
from discord import Embed
import os
from Util import logger

# import config
try:
    import config
except ImportError:
    print("Couldn't import config.py! Exiting!")
    exit()

stream = discord.Streaming(name="Hero's channel on Twitch!", url="https://www.twitch.tv/herogamers",
                               twitch_name="herogamers")
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=os.getenv('prefix'), description='I guess this is a bot, it does bot things.',
                   activity=stream, intents=intents)

startup_extensions = ["essentials",
                      "info",
                      "Tasks"]


# For checking the welcome channel
async def welcome_channel():
    # Defining bot messages for the welcome channel
    welcomeembeds = []
    # --- Welcome image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://cdn.discordapp.com/attachments/237223522710192129/684481561084952671/welcomepic-treeland.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Welcome message ---
    embed = discord.Embed(title="Welcome to Treeland!", color=discord.Color.from_rgb(255, 105, 180),
                          description="Hi, welcome to Treeland! <a:bugcatwiggle2:564875858767118356>\n\n"
                                      
                                      "You can see Treeland as your new home, away from home. A second family. "
                                      "We want to keep a civil tone in here, whilst still having heck loads of fun.\n\n"
                                      
                                      "If you need help with anything, go ahead and ping an active "
                                      "<@&222000308182712320>, but please only ping if you find it necessary, "
                                      "or else you might get your ass whooped.\n"
                                      "If you think something should be added, removed or changed, "
                                      "please send it into a Staff's DM's, in a clean and clear way "
                                      "<:KKomrade:590630277710348288>\n\n"
                                      
                                      "We don't want to bore someone to death with a huge list of rules, so we only "
                                      "have a few, but we still expect all of you to follow them "
                                      "<a:hugheart:646102861243088925>")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/237223522710192129/1018543998840873060/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Rules image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://cdn.discordapp.com/attachments/237223522710192129/684476798092050492/rules-treeland.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Rules message ---
    embed = discord.Embed(title="The Rules of Treeland", color=discord.Color.from_rgb(255, 105, 180),
                          description='*"So... You want to hear a story, eh? One about treasure hunters? '
                                      'Haha, have I got a story for you!"* - Wait, wrong transcript...\n'
                                      "Well, to become a fully-fledged Treelander you've got to know your way around "
                                      "our rules, but fret not! They are quite simple:\n\n\n"

                                      # Rule 1
                                      "**1.** Behave properly to others.\n\n"
                                      # Rule 2
                                      "**2.** No NSFW content in channels that aren't marked as NSFW. "
                                      "Explicit pornographic content isn't allowed anywhere in Treeland.\n\n"
                                      # Rule 3
                                      "**3.** Don't break the [Discord Terms of Service](https://dis.gd/terms).\n\n"
                                      # Rule 4
                                      "**4.** Stick to the [Discord Community Guidelines](https://dis.gd/guidelines) "
                                      "(as well as the [Discord Partnership Code of Conduct]("
                                      "https://dis.gd/partnercoc)).")
    embed.set_footer(text="The Treeland Community - Our rules are subject to change without notice.", icon_url="https://cdn.discordapp.com/attachments/237223522710192129/1018543998840873060/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Roles image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://cdn.discordapp.com/attachments/237223522710192129/684477910987440159/roles-treeland.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Roles message ---
    embed = discord.Embed(title="The Roles of Treeland", color=discord.Color.from_rgb(255, 105, 180),
                          description="Now... What are those shiny Roles I see in the side panel?\n"
                                      "Well... allow me to explain\n\n"

                                      "**:green_heart: 🢡 Treelander of the Day:** A random member of Treeland chosen "
                                      "every day at 12 PM (CET). Gets access to write in <#647828868782358539>.\n"
                                      "\n"
                                      "**:purple_heart: 🢡 Royalty of Treeland:** These people are true followers of "
                                      "Treeland, and have been for many many years.\n"
                                      "**:blue_heart: 🢡 Epic Gamers:** People in this role are either freakin' "
                                      "awesome and are a part of our staff team <3\n"
                                      "**:seedling: 🢡 Master Tree Grower:** This role is given to "
                                      "people who are very good at growing our trees here in Treeland, by boosting "
                                      "our small land with their Nitro Boost!\n"
                                      "\n"
                                      "**:evergreen_tree: 🢡 Evergreen:** To go even further beyond. This individual "
                                      "is either to be feared or looked down upon, as they clearly have given their "
                                      "souls away and dedicated themselves to Treeland. Reached at a whoppin' 50000 "
                                      "Server Exp.\n"
                                      "**:tanabata_tree: 🢡 Tanabata:** Wowie, now we're gettin' there. If an "
                                      "individual has this role, you should know that they know their shit. Reached "
                                      "at 10000 Server Exp.\n"
                                      "**:palm_tree: 🢡 Palm:** An individual who has this role should know what's "
                                      "happening around here by now. Reached at Level 5000 Server Exp.\n"
                                      "**:deciduous_tree: 🢡 Treelander:** This role is given to people who have "
                                      "reached 500 Server Exp, and those people are now a fully fledged citizen of "
                                      "Treeland.\n"
                                      "**:smiling_face_with_3_hearts: 🢡 Peeps:** This role is given to people who "
                                      "joined at the Invite-only stage of the Heroji Emote Servers.\n"
                                      "**:earth_africa: 🢡 IRL:** This role is given to people who I know and have "
                                      "met physically.\n"
                                      "**:balloon: 🢡 Risings:** You might be familiar with this role, well it's the "
                                      "role you got when you first got here. It's the role for people that are on "
                                      "their way up the rankings.\n")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/237223522710192129/1018543998840873060/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Invite image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://cdn.discordapp.com/attachments/237223522710192129/684492613038243860/socials-treeland.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Invite message ---
    embed = discord.Embed(title="Treeland's Socials", color=discord.Color.from_rgb(255, 105, 180),
                          description="So, we bet you're totally ecstatic about inviting your Friends and Family to "
                                      "Treeland right now! Well, fret not, we've got you covered with all sorts of "
                                      "magic ways to keep in touch with Treeland, no matter where you are!\n\n"
                                      
                                      "**Reddit** - [r/HeroGamers](https://www.reddit.com/r/HeroGamers/)\n"
                                      "**Twitch** - [HeroGamers](https://www.twitch.tv/herogamers)\n"
                                      "**Twitter** - [@TheTreeland](https://twitter.com/TheTreeland)\n"
                                      "**Discord** - [discord.gg/PvFPEfd](https://discord.gg/PvFPEfd) or "
                                      "[treeland.herogamers.xyz](https://treeland.herogamers.xyz)")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/237223522710192129/1018543998840873060/Treeland2.gif")
    welcomeembeds.append(embed)
    # --- Opt-in/opt-out roles image ---
    embed = discord.Embed(color=discord.Color.from_rgb(255, 105, 180))
    embed.set_image(url="https://cdn.discordapp.com/attachments/237223522710192129/684479344059744268/optroles-treeland.png")
    welcomeembeds.append(embed)  # Append the created embed
    # --- Opt-in/opt-out roles message ---
    embed = discord.Embed(title="Opt-in/Opt-out Roles", color=discord.Color.from_rgb(255, 105, 180),
                          description="Currently you should not have any of these roles! These roles are used for "
                                      "various purposes, such as to ping you, the user, when there is something going "
                                      "on in here, so we don't have to use the atEveryone all the time. So, "
                                      "here are the roles, what they do, and how you opt-in (or opt-out for them):\n\n"

                                      "<:POGGIES:586184959254069258> **pingpong:** You get pinged for Treeland stuff, "
                                      "like when we go live on Twitch or other community events!\n"
                                      "<a:catblushINTENSE:587309010500452352> **free game:** You get pinged when "
                                      "there is a free game to be grabbed. Free, and games? WHO CAN SAY NO TO THAT??\n"
                                      "<a:ricardoFlick:590695048564178944> **adult:** [18+] You get access to a "
                                      "channel where discussions of NSFW content is allowed. This includes "
                                      "discussions of nudity, sexuality and violence. Note that explicit pornographic "
                                      "content still has no place in Treeland.\n"
                                      "<:denyhammer:586250559653281809> **botsupport:** Are you here in need of "
                                      "Support for bots developed by Hero (like WatchDog)? Get yourself the "
                                      "botsupport role!\n"
                                      "<:sad:750066286872232056> **anti-totd: Are you tired of getting randomly "
                                      "pinged just to let you know that today YOU are awesome and special? Well, "
                                      "fine then - not like we liked you anyway, b-baka! >//<\n"
                                      "\n "
                                      "***To opt for the roles, react to this message with the emotes used above!***")
    embed.set_footer(text="The Treeland Community", icon_url="https://cdn.discordapp.com/attachments/237223522710192129/1018543998840873060/Treeland2.gif")
    welcomeembeds.append(embed)


    # Editing the current bot messages, if they aren't identical with the ones defined above
    channel = bot.get_channel(221996778092888065)  # channel is #welcome

    current_botmessages = []
    async for message in channel.history(limit=20):
        if message.author == bot.user:
            current_botmessages.append(message)
    # Reverse because it reads from the bottom up
    current_botmessages.reverse()

    # Checking if they are identical to welcomeembeds content
    embed_index = 0
    for embed in welcomeembeds:
        # If there aren't the same amount of messages
        # if len(welcomeembeds) != len(current_botmessages):

        type = None
        if embed.image != Embed.Empty:
            type = "Image"
        elif embed.description != Embed.Empty:
            type = "Message"
        else:
            await logger.log("Error! Embed has no image nor message", bot, "ERROR")
            continue

        # Looking if a message has been posted at this embed index yet
        current_message = None
        try:
            current_message = current_botmessages[embed_index]
        except IndexError:
            logger.logDebug("No message for this yet")

        # If message exists
        if current_message is not None:
            # For images
            if type == "Image":
                if current_message.embeds[0].image != Embed.Empty:
                    if current_message.embeds[0].image.url != embed.image.url:
                        await current_message.edit(embed=embed)
            # For messages
            if type == "Image":
                if current_message.embeds[0].description != Embed.Empty:
                    if current_message.embeds[0].description != embed.description:
                        await current_message.edit(embed=embed)
        else: # Otherwise, just send the embed as a new message
            await channel.send(embed=embed)

        embed_index += 1


@bot.event
async def on_connect():
    # Bot startup is now done...
    logger.logDebug("----------[LOGIN SUCESSFULL]----------", "INFO")
    logger.logDebug("     Username: " + bot.user.name, "INFO")
    logger.logDebug("     UserID:   " + str(bot.user.id), "INFO")
    logger.logDebug("--------------------------------------", "INFO")
    print("\n")

    logger.logDebug("The bot is ready!", "INFO")
    print("\n")


@bot.event
async def on_ready():
    logger.logDebug("Prunus has (re)connected to Discord!")

    logger.logDebug("Checking the welcome channel!", "INFO")
    await welcome_channel()
    logger.logDebug("Done checking the welcome channel!", "INFO")
    print("\n")


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
        await logger.log(error, bot, "ERROR")

@bot.event
async def on_guild_join(guild):
    await logger.log("Joined a new guild (`%s` - `%s`)" % (guild.name, guild.id), bot, "INFO")

@bot.event
async def on_member_update(before, after):
    for role in before.roles:
        if role.id == 530778945105428501:
            return
    for role in after.roles:
        if role.id == 530778945105428501:
            emojis = bot.emojis
            emote = u"\U0001F4E5"
            for emoji in emojis:
                if emoji.id == 561907145231171625:
                    emote = "<:" + emoji.name + ":" + str(emoji.id) + ">"
                    break
            
            channel = bot.get_channel(665922203686273054)

            embed = discord.Embed(title="Welcome to Treeland, " + after.display_name, color=discord.Color.from_rgb(255, 105, 180), timestamp=datetime.datetime.utcnow(),
                description=emote + " <@" + str(after.id) + "> just became a member of Treeland! Please welcome them!")
            embed.set_footer(text="New Member of Treeland", icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
            embed.set_thumbnail(url=after.avatar_url)
            await channel.send(embed=embed)
            await logger.log("A member just got the rising role... %s#%s" % (after.name, after.discriminator), bot, "INFO")

@bot.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    ctx:commands.Context = await bot.get_context(message)
    if message.content.startswith(os.getenv('prefix')):
        if ctx.command is not None:
            await logger.log("`%s` (%s) used the `%s` command in the guild `%s` (%s), in the channel `%s` (%s)" % (ctx.author.name, ctx.author.id, ctx.invoked_with, ctx.guild.name, ctx.guild.id, ctx.channel.name, ctx.channel.id), bot, "INFO")
            await bot.invoke(ctx)
    else:
        return

if __name__ == '__main__':
    # we setup the logger first
    logger.setup_logger()
    # load extensions
    for extension in startup_extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            logger.log(f"Failed to load extension {extension}. - {e}", bot, "ERROR")
    bot.load_extension("jishaku")

try:
    bot.run(os.getenv('token'))
except Exception as e:
    logger.logException("Running bot exception!", e)
