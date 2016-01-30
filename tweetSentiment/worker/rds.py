__author__ = 'yazhu'
import redis
from django.conf import settings


class Redis(object):
    _instance = None
    _redis = redis.StrictRedis(settings.REDIS['host'], settings.REDIS['port'], settings.REDIS['db'])

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Redis, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def getRedis(self):
        return self._redis