import datetime
import random
import discord
from discord.ext import tasks, commands
import PrunusDB
from Util import logging


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.treelanderOfTheDay.start()

    def cog_unload(self):
        self.treelanderOfTheDay.cancel()

    @tasks.loop(seconds=30.0)
    async def treelanderOfTheDay(self):
        logging.logDebug("Treelander of the day Task")
        totD_id = PrunusDB.get_currentTreelanderOfTheDay()
        logging.logDebug("totD_id: " + totD_id)
        dt = datetime.datetime.now()
        logging.logDebug("dt: " + str(dt))
        if totD_id == "" or len(totD_id) == 0:
            logging.logDebug("aaaaaaa")
            await self.newTreelanderOfTheDay(totD_id)
        elif dt.time() > datetime.time(12):
            logging.logDebug("it is over 12. Time now is: " + str(datetime.datetime.now().time()))
            treelanderOfTheDayTime = PrunusDB.get_currentTreelanderOfTheDayTime()
            logging.logDebug(treelanderOfTheDayTime)
            current_treelanderOfTheDay_TimeStamp = datetime.datetime.strptime(str(treelanderOfTheDayTime),
                                                                              "%Y-%m-%d %H:%M:%S.%f")
            logging.logDebug("yes")
            logging.logDebug(str(current_treelanderOfTheDay_TimeStamp))

            timeElapsed = dt - current_treelanderOfTheDay_TimeStamp
            logging.logDebug(timeElapsed)
            timeElapsed_seconds = timeElapsed.total_seconds()
            logging.logDebug(timeElapsed_seconds)
            timeElapsed_hours = divmod(timeElapsed.total_seconds(), 3600)[0]
            logging.logDebug(timeElapsed_hours)
            if timeElapsed_hours > 20:
                logging.logDebug("it was now over 20 hours ago")
                await self.newTreelanderOfTheDay(totD_id)
        else:
            logging.logDebug("suck")

    @treelanderOfTheDay.before_loop
    async def before_loop(self):
        logging.logDebug('waiting...')
        await self.bot.wait_until_ready()

    async def newTreelanderOfTheDay(self, totD_id=""):
        logging.logDebug('newtreelanderoftheday')
        logging.logDebug("nice totD_id: " + totD_id)
        treeland = self.bot.get_guild(221996778092888065)
        logging.logDebug('got treeland')
        treelanders = treeland.members
        logging.logDebug('got members')
        while True:
            logging.logDebug('while loop')
            user = random.choice(treelanders)
            logging.logDebug('got random user: ' + user.name)
            if user.bot:
                logging.logDebug("user is a bot")
            elif totD_id == "" or len(totD_id) == 0:
                logging.logDebug('todays treelander id is 0, found new treelander of the day')
                break
            elif totD_id == str(user.id):
                logging.logDebug("User is already treelander of the day")
            else:
                logging.logDebug('new treelander of the day found!')
                break
            logging.logDebug("help")
        logging.logDebug('out of while loop')
        await user.add_roles(638480387403677727, reason="Treelander of the Day!")
        logging.logDebug('added role')
        await PrunusDB.add_TreelanderOfTheDay(user.id, user.name + user.discriminator, self.bot)
        if totD_id != "" and len(totD_id) != 0:
            logging.logDebug("is not empty")
            totD = self.bot.get_user(int(totD_id))
            logging.logDebug("got user: " + totD.name)
            if totD is not None:
                logging.logDebug("user is not null")
                await totD.remove_roles(638480387403677727, reason="No longer the Treelander of the Day!")
                logging.logDebug('removed role')
                PrunusDB.remove_TreelanderOfTheDay(totD_id)
        logging.logDebug("sending embed")

        channel = self.bot.get_channel(221998962247204864)

        emojis = self.bot.emojis
        for emoji in emojis:
            if emoji.id == 584529307402240000:
                emote = "<:" + emoji.name + ":" + str(emoji.id) + ">"
                break
            emote = u"\U0001F333"

        embed = discord.Embed(title="New Treelander of the Day!",
                              color=discord.Color.from_rgb(22, 198, 12), timestamp=datetime.datetime.utcnow(),
                              description=emote + " <@" + str(
                                  user.id) + "> just became a member of Treeland! Please welcome them!")
        embed.set_footer(text="New Treelander of the Day",
                         icon_url="https://cdn.discordapp.com/attachments/513770658589704204/588464009217310771/Treeland2.gif")
        embed.set_thumbnail(url=user.avatar_url)
        await channel.send(embed=embed)
        await logging.log(
            "**[Info]** A member just became Treelander of the Day... %s#%s" % (user.name, user.discriminator),
            self.bot)


def setup(bot):
    bot.add_cog(Tasks(bot))
