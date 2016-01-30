from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core import serializers
from models import Company, SecForm
import json
import urllib
from valueCrawler.crawlFunction.companies import getAllCompanies


class GetSymbolGraph(TemplateView):
    template_name = 'secTest.html'

    def get(self, request, *args, **kwargs):
        response = super(GetSymbolGraph, self).get(request, *args, **kwargs)
        response.context_data['symbol'] = kwargs['symbol']
        response.context_data['companyNum'] = len(Company.objects.all())
        response.context_data['formNum'] = len(SecForm.objects.all())
        company = get_list_or_404(Company, symbol=kwargs['symbol'])
        response.context_data['companyOverview'] = serializers.serialize('json', company)
        return response


class GetAllCompaniesInfo(TemplateView):
    template_name = 'secTest.html'

    def get(self, request, *args, **kwargs):
        response = super(GetAllCompaniesInfo, self).get(request, *args, **kwargs)
        response.context_data['companyNum'] = len(Company.objects.all())
        response.context_data['formNum'] = len(SecForm.objects.all())
        return response


class GetSymbolAllForms(TemplateView):
    template_name = 'forms.html'

    def get(self, request, *args, **kwargs):
        response = super(GetSymbolAllForms, self).get(request, *args, **kwargs)
        response.context_data['symbol'] = kwargs['symbol']
        company = get_object_or_404(Company, symbol=kwargs['symbol'])
        forms = get_list_or_404(SecForm, company=company)
        response.context_data['forms'] = serializers.serialize('json', forms)
        return response