from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class keyWordToSentiment(TemplateView):
    template_name = 'secTest.html'

    def get(self, request, *args, **kwargs):
        response = super(keyWordToSentiment, self).get(request, *args, **kwargs)

        response.context_data['symbol'] = kwargs['symbol']
        company = get_list_or_404(Company, symbol=kwargs['symbol'])
        response.context_data['companyOverview'] = serializers.serialize('json', company)
        return response