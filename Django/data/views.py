from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import json 
import codecs
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from data.models import Customer


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)



#json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')

class JsonM(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataM = json.load(json_data)['Morbilidad_Adolescente']
        return JsonResponse(dataM,safe=False)
        


class JsonR(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataR = json.load(json_data)['Riesgo_Adolescente']
        return JsonResponse(dataR,safe=False)

 
class JsonT(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataT = json.load(json_data)['Tamizaje_Adolescente']
        return JsonResponse(dataT,safe=False)       


class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')


@api_view(["POST"])
def CalcTest(x1):
    try:
        x=json.loads(x1.body)
        y=str(x*100)
        return JsonResponse("Result:"+y,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


class CustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'type')


class CustViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustSerializer
