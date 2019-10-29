import praw
import os
from Util import logging

reddit = praw.Reddit(user_agent=os.getenv('reddit_bot_name'),
                     client_id=os.getenv('reddit_bot_id'), client_secret=os.getenv('reddit_bot_secret'),
                     username=os.getenv('reddit_username'), password=os.getenv('reddit_password'))

subreddit = reddit.subreddit(os.getenv('reddit_subreddit'))

def setFlair(user, flair):
    if flair == "Treelander":
        subreddit.flair.set(redditor=user, flair_template_id="8f0d65e0-b2f2-11e9-9482-0eae0a1be154")
    elif flair == "Palm":
        subreddit.flair.set(redditor=user, flair_template_id="fc3f38b4-b45a-11e9-b8a3-0e51cd86f754")
    elif flair == "Tanabata":
        subreddit.flair.set(redditor=user, flair_template_id="08619f24-b45b-11e9-b02b-0eab0b9f7ee0")
    elif flair == "Evergreen":
        subreddit.flair.set(redditor=user, flair_template_id="13c10b2a-b45b-11e9-b948-0e4c5381977e")
    elif flair == "Master Tree Grower":
        subreddit.flair.set(redditor=user, flair_template_id="2c75aef0-b45b-11e9-ae25-0e3307dfb7be")
    elif flair == "IRL":
        subreddit.flair.set(redditor=user, flair_template_id="23af63ec-b45b-11e9-8717-0e15d979c804")
    else:
        return