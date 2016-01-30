__author__ = 'yazhu'
from twython import Twython
from tweetSentiment.models import TweetAuth
from django.conf import settings


class twitter(object):
    APP_KEY = None
    APP_SECRET = None
    ACCESS_TOKEN = None
    ACCESS_SECRET = None
    twitter_instance = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(twitter, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not self.APP_KEY:
            self.APP_KEY = settings.TWEETER_SETTINGS['APP_KEY']
        if not self.APP_SECRET:
            self.APP_SECRET = settings.TWEETER_SETTINGS['APP_SECRET']
        if not self.ACCESS_TOKEN:
            self.ACCESS_TOKEN = settings.TWEETER_SETTINGS['ACCESS_TOKEN']
        if not self.ACCESS_SECRET:
            self.ACCESS_SECRET = settings.TWEETER_SETTINGS['ACCESS_SECRET']
        if not self.twitter_instance:
            self.twitter_instance = Twython(self.APP_KEY, self.APP_SECRET,
                                            self.ACCESS_TOKEN, self.ACCESS_SECRET)

    def getOUAH(self):
        #step one: get tmp token and secret, and send out final token request
        twr = Twython(self.APP_KEY, self.APP_SECRET)
        auth = twr.get_authentication_tokens(callback_url=settings.TWEETER_SETTINGS['CALLBACK_URL'])
        self.ACCESS_TOKEN = auth['oauth_token']
        self.ACCESS_SECRET = auth['oauth_token_secret']

    def updateOUAHWithVerifier(self, oauth_verifier):
        twitter = Twython(self.APP_KEY, self.APP_SECRET,
                          self.ACCESS_TOKEN, self.ACCESS_SECRET)
        final_token = twitter.get_authorized_tokens(oauth_verifier)
        self.__refreshToken(final_token)

    def __refreshToken(self, auth):
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
        self.ACCESS_TOKEN = OAUTH_TOKEN
        self.ACCESS_SECRET = OAUTH_TOKEN_SECRET
        self.twitter_instance = Twython(self.APP_KEY, self.APP_SECRET,
                                        self.ACCESS_TOKEN, self.ACCESS_SECRET)
        #And store new token in db as backup
        newAuth = TweetAuth.objects.filter(appName=settings.TWEETER_SETTINGS['APP_NAME'])
        if not newAuth:
            newAuth = TweetAuth()
        newAuth.appAccessSecret = self.ACCESS_SECRET
        newAuth.appAccessToken = self.ACCESS_TOKEN
        newAuth.appKey = self.APP_KEY
        newAuth.appName = settings.TWEETER_SETTINGS['APP_NAME']
        newAuth.appSecret = self.APP_SECRET
        newAuth.save()
