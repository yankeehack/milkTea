from django.conf.urls import url
from views import GetSymbolGraph, GetAllCompaniesInfo

urlpatterns = [
    url(r'^graph/(?P<symbol>[a-zA-Z]+)/', GetSymbolGraph.as_view()),
    url(r'^graph/', GetAllCompaniesInfo.as_view())

]