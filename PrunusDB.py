from peewee import SqliteDatabase, Model, CharField, DateTimeField, BooleanField, IntegrityError, CompositeKey
import datetime
from Util import logger

db = SqliteDatabase('./prunusDB.db')


class TreelanderOfTheDay(Model):
    Time = DateTimeField(unique=True)
    UserID = CharField()
    DiscordTag = CharField()
    IsTreelanderOfTheDay = BooleanField()

    class Meta:
        database = db


async def add_TreelanderOfTheDay(userid, name, bot):
    date = datetime.datetime.now()
    try:
        TreelanderOfTheDay.create(UserID=userid, DiscordTag=name, Time=date,
                                  IsTreelanderOfTheDay=True)
    except IntegrityError as e:
        await logger.log("DB Notice: Date Already Used! - " + str(e), bot, "DEBUG")


def remove_TreelanderOfTheDay(userid, deepRemoval):
    if deepRemoval:
        query = TreelanderOfTheDay.update(IsTreelanderOfTheDay=False).where(TreelanderOfTheDay.UserID != userid)
    else:
        query = TreelanderOfTheDay.update(IsTreelanderOfTheDay=False).where(TreelanderOfTheDay.UserID == userid)
    query.execute()


def get_currentTreelanderOfTheDay():
    query = TreelanderOfTheDay.select().where(TreelanderOfTheDay.IsTreelanderOfTheDay == True)
    try:
        return query[0].UserID
    except IndexError:
        return ""


def get_currentTreelanderOfTheDayTime():
    query = TreelanderOfTheDay.select().where(TreelanderOfTheDay.IsTreelanderOfTheDay == True)
    try:
        return query[0].Time
    except IndexError:
        return ""


class FreeGames(Model):
    Title = CharField(null=False)
    From = DateTimeField(null=False, default=datetime.datetime.now())
    To = DateTimeField(null=False)
    Platform = CharField(null=False)

    class Meta:
        primary_key = CompositeKey("Title", "From", "To", "Platform")
        database = db


def new_free_game(title, startdate, enddate, platform="epicgames"):
    try:
        FreeGames.create(Title=title, From=startdate, To=enddate, Platform=platform)
    except IntegrityError as e:
        logger.logDebug("Couldn't add free game: " + str(e))


def get_free_game(title, platform=None):
    if not platform:
        query = FreeGames.select().where(FreeGames.Title == title)
    else:
        query = FreeGames.select().where((FreeGames.Title == title) & (FreeGames.Platform == platform))

    if query.exists():
        return query
    return []


def get_free_game_checked(title, platform=None, time=datetime.datetime.now()):
    if not platform:
        query = FreeGames.select().where((FreeGames.Title == title) & (FreeGames.From <= time) & (time <= FreeGames.To))
    else:
        query = FreeGames.select().where((FreeGames.Title == title) & (FreeGames.Platform == platform) & (FreeGames.From <= time) & (time <= FreeGames.To))

    if query.exists():
        return query
    return None



def create_tables():
    with db:
        db.create_tables([TreelanderOfTheDay, FreeGames])


create_tables()
