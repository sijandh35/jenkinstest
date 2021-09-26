from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import requests
import json
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from core.models import StockLog, StockName


# filters = {}

# for key, value in request.post.items():
#     if key in ['filter1', 'filter2', 'filter3']:
#         filters[key] = value

# Test.objects.filter(**filters)

# filters = {
#     key: value
#     for key, value in request.post.items()
#     if key in ['filter1', 'filter2', 'filter3']
# }

# Test.objects.filter(**filters)

class NepseApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    # def get(self, request, format=None):
    #     return JsonResponse(data,safe=False)

    def get(self, request, *args, **kwargs):
        r = requests.get('https://nepse-data-api.herokuapp.com/data/todaysprice', params=request.GET)
        data = r.json()
        for v in StockName.objects.all():
            f = filter(lambda d: d['companyName'] == v.name ,data)
            v.log.create(json=json.dumps(list(f)[0]),stock_name=v.name)
        return Response({'stock_data': data}, template_name='index.html')