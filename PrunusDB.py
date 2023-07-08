import pymysql
from peewee import SqliteDatabase, Model, CharField, DateTimeField, BooleanField, MySQLDatabase, InternalError, \
    IntegrityError, CompositeKey
import datetime
import os
from Util import logger

# Initiation of database
if os.getenv('db_type') is not None and os.getenv('db_type').upper() == "MYSQL":
    while True:
        host = "localhost"
        if os.getenv("MARIADB_HOST"):
            host = os.getenv("MARIADB_HOST")
        elif os.getenv('db_host'):
            host = os.getenv('db_host')
        else:
            print("Database host is empty, using " + host + " as host...")

        user = "root"
        if os.getenv("MARIADB_USER"):
            user = os.getenv("MARIADB_USER")
        elif os.getenv('db_user'):
            user = os.getenv('db_user')
        else:
            print("Database user is empty, using " + user + " as user...")

        port = "3306"
        if os.getenv("MARIADB_PORT"):
            port = os.getenv("MARIADB_PORT")
        elif os.getenv('db_port'):
            port = os.getenv('db_port')
        else:
            print("Database port is empty, using " + port + " as port...")

        database_name = "prunus"
        if os.getenv('MARIADB_DATABASE'):
            database_name = os.getenv('MARIADB_DATABASE')

        password = None
        if os.getenv("MARIADB_PASSWORD"):
            password = os.getenv("MARIADB_PASSWORD")
        elif os.getenv('db_pword'):
            password = os.getenv('db_pword')

        print("Connecting to database " + database_name + " on " + host + ":" + port + " as " + user + "...")

        db = MySQLDatabase(database_name, user=user, password=password, host=host,
                           port=int(port))

        # Check for possible connection issues to the db
        try:
            db.connection()
            break
        except Exception as e:
            if "Can't connect" in str(e):
                print("An error occured while trying to connect to the MySQL Database: " + str(e) + ". Trying again...")
            elif "Unknown database" in str(e):
                print("An error occured while trying to connect to the MySQL Database: " + str(e) +
                      ". Trying to create database...")
                try:
                    conn = pymysql.connect(host=host, user=user, password=password, port=int(port))
                    conn.cursor().execute('CREATE DATABASE ' + database_name)
                    conn.close()
                    print("Created Database!")
                    break
                except Exception as e:
                    print("An error occured while trying to create the prunus Database: " + str(e) + ". Trying again...")
        except InternalError as e:
            print("An error occured while trying to use the MySQL Database: " + str(e) + ". Trying again...")
else:
    print("Database type is not set to MYSQL, using flatfile...")
    db = SqliteDatabase('./prunusDB.db', pragmas={'foreign_keys': 1})


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
        return True
    except IntegrityError as e:
        logger.logDebug("Couldn't add free game: " + str(e))
    return False


def get_free_game(title, platform=None):
    if not platform:
        query = FreeGames.select().where(FreeGames.Title == title)
    else:
        query = FreeGames.select().where((FreeGames.Title == title) & (FreeGames.Platform == platform))

    if query.exists():
        return query
    return []


def get_free_game_checked(title, platform=None, time=datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)):
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
