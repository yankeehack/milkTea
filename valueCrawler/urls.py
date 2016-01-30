from django.conf.urls import url
from views import GetSymbolGraph, GetAllCompaniesInfo, GetSymbolAllForms

urlpatterns = [
    url(r'^graph/(?P<symbol>[a-zA-Z]+)/forms', GetSymbolAllForms.as_view()),
    url(r'^graph/(?P<symbol>[a-zA-Z]+)', GetSymbolGraph.as_view()),
    url(r'^graph/', GetAllCompaniesInfo.as_view())

]