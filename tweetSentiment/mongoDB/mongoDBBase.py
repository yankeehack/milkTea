__author__ = 'yazhu'
from twython import Twython
from tweetSentiment.models import TweetAuth
from django.conf import settings
from pymongo import MongoClient


class mongoBase(object):
    mongo_connection = None

    def __init__(self):
        super(mongoBase, self).__init__()
        self.mongo_connection = MongoClient(settings.MONGODB['MONGODB_HOST'], settings.MONGODB['MONGODB_PORT'])


