from django.conf.urls import url
from views.views import keyWordToSentiment
urlpatterns = [
    url(r'^twitterApi/', keyWordToSentiment.as_view()),
]