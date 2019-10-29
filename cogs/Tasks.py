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

    @tasks.loop(seconds=5.0)
    async def treelanderOfTheDay(self):
        totD_id = PrunusDB.get_currentTreelanderOfTheDay()
        if totD_id == "" or len(totD_id) == 0:
            await self.newTreelanderOfTheDay(self)
        elif datetime.datetime.now().time() > datetime.time(12):
            current_treelanderOfTheDay_TimeStamp = datetime.datetime.parse(PrunusDB.get_currentTreelanderOfTheDayTime())
            if (datetime.datetime.now() - current_treelanderOfTheDay_TimeStamp) > 20:
                await self.newTreelanderOfTheDay(self)

    async def newTreelanderOfTheDay(self, totD_id=""):
        treeland = self.bot.get_guild(self, 221996778092888065)
        treelanders = treeland.members
        notFound = True
        while notFound:
            user = random.choice(treelanders)
            if totD_id == "" or len(totD_id) == 0:
                notFound = False
            elif totD_id == user.id:
                logging.log("User is already treelander of the day", self.bot, "DEBUG")
            else:
                notFound = False
        await user.add_roles(638480387403677727, reason="Treelander of the Day!")
        await PrunusDB.add_TreelanderOfTheDay(user.id, user.name + user.discriminator, self.bot)
        if totD_id != "" or len(totD_id) != 0:
            totD = self.bot.get_user(self, totD_id)
            if totD != None:
                await totD.remove_roles(638480387403677727, reason="No longer the Treelander of the Day!")
                PrunusDB.remove_TreelanderOfTheDay(totD_id)

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
