from django.db import models

# Create your models here.


class Tweet(models.Model):
    keyword = models.CharField(max_length=200, default="")
    user = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=500, default="")
    latitude = models.CharField(max_length=255, default="")
    longitude = models.CharField(max_length=255, default="")
    sicDescription = models.CharField(max_length=100, default="")
    createTime = models.DateTimeField(auto_now_add=True)
    lastModifiedTime = models.DateTimeField(auto_now=True)
    sentiment_exist = models.BooleanField(default=False)
    sentiment = models.FloatField(null=True)
    pass


class TweetAuth(models.Model):
    appName = models.CharField(max_length=200, default="")
    appSecret = models.CharField(max_length=200, default="")
    appKey = models.CharField(max_length=200, default="")
    appAccessToken = models.CharField(max_length=200, default="")
    appAccessSecret = models.CharField(max_length=200, default="")
    pass


