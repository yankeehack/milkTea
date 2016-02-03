from django.conf.urls import url
from views.views import keyWordToSentiment
from views.dashBoardViews import mainView, projectsJsonView
urlpatterns = [
    url(r'^twitterApi/', keyWordToSentiment.as_view()),
    url(r'^dashboard/', mainView.as_view()),
    url(r'^donorschoose/projects/', projectsJsonView.as_view())
]