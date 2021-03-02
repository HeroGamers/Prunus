import os, sys, logging, datetime, discord
from logging.handlers import TimedRotatingFileHandler

from discord import Embed


def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%H:%M:%S')

    handler = TimedRotatingFileHandler("logs/Prunus.log", when="midnight", interval=1, encoding="UTF-8")
    handler.suffix = "%Y%m%d"
    handler.setFormatter(formatter)

    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)

    logger = logging.getLogger("Prunus")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)  # CAN BE CHANGED TO "logging.DEBUG", when run locally to enable debugging!
    logger.addHandler(screen_handler)


async def log(message, bot, level="INFO", debug=""):
    # Return if the logging level is not DEBUG, and the bot is trying to log some debugging stuff
    logger = logging.getLogger("Prunus")
    if (logger.getEffectiveLevel != logging.DEBUG) and (level == "DEBUG"):
        return

    logChannel = bot.get_channel(int(os.getenv('botlog')))
    time = datetime.datetime.now().strftime('%H:%M:%S')

    if level == "ERROR":
        levelemote = "❌"
    elif level == "CRITICAL":
        levelemote = "🔥"
    elif level == "WARNING":
        levelemote = "❗"
    elif level == "DEBUG":
        levelemote = "🔧"
    else:
        levelemote = "🔎"

    await logChannel.send("`[" + time + "]` **" + levelemote + " " + level + ":** " + message)

    if debug == "":
        logDebug(message, level)
        return
    logDebug(debug, level)


def logDebug(message, level="INFO"):
    logger = logging.getLogger("Prunus")

    if level == "DEBUG":
        logger.debug(message)
    elif level == "CRITICAL":
        logger.critical(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    else:
        logger.info(message)


async def logCommand(commandName, ctx, level="INFO"):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await log(ctx.author.name + "#" + ctx.author.discriminator + " just ran the " + commandName + " command",
                  ctx.bot, level)
    else:
        await log(
            ctx.author.name + "#" + ctx.author.discriminator + " just ran the " + commandName + " command, in the channel #" + ctx.channel.name + " (`" + str(
                ctx.channel.id) + "`), in the guild " + ctx.guild.name + " (`" + str(ctx.guild.id) + "`)", ctx.bot,
            level)


async def logEmbed(color, description, bot, debug=""):
    channel = bot.get_channel(int(os.getenv('botlog')))
    await channel.send(embed=Embed(color=color, description=description))
    if debug == "":
        logDebug(description)
        return
    logDebug(debug)


def logException(message, error):
    logger = logging.getLogger("Prunus")

    logger.exception(message, exc_info=(type(error), error, error.__traceback__))
