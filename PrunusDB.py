from peewee import SqliteDatabase, Model, CharField, DateTimeField, BooleanField, IntegrityError
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


def create_tables():
    with db:
        db.create_tables([TreelanderOfTheDay])


create_tables()
