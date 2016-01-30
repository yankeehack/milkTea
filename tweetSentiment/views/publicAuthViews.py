__author__ = 'yazhu'
from django.views.generic import View
from tweetSentiment.tweetApi.tweetGet import twitter
from django.http import HttpResponse, HttpResponseForbidden


class twitterAuthView(View):
    def get(self, request, *args, **kwargs):
        oauth_verifier = request.GET['oauth_verifier']
        if oauth_verifier:
            tr = twitter()
            tr.updateOUAHWithVerifier(oauth_verifier)
            return HttpResponse()
        else:
            return HttpResponseForbidden()
