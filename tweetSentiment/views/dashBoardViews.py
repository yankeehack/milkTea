__author__ = 'yazhu'
from django import http
from django.views.generic import TemplateView
from tweetSentiment.mongoDB.MongoDBProjectsCollections import mongoBaseProjectsCollections
import json
from bson import json_util
from bson.json_util import dumps

class mainView(TemplateView):
    template_name = 'dashboard.html'


class projectsJsonView(TemplateView):
    def get_context_data(self, **kwargs):
        # override existing single object view
        collections = mongoBaseProjectsCollections()
        projects = collections.getProjects()
        dict_projects = []
        for project in projects:
            dict_projects.append(project)
        collections.closeConnection()
        return dict_projects

    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context, default=json_util.default)
