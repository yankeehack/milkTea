from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from tweetSentiment.tweetApi.tweetGet import twitter
import json


class keyWordToSentiment(TemplateView):
    template_name = 'twitterDisplay.html'

    def get(self, request, *args, **kwargs):
        tw = twitter()
        test = tw.twitter_instance.search(q='twitter', result_type='popular')
        response = super(keyWordToSentiment, self).get(request, *args, **kwargs)
        response.context_data['test'] = test
        return response