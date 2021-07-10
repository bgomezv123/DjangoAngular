from django.conf.urls import url
from django.urls import path, include

from data import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', views.CustViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$', views.LinksPageView.as_view()),
    url(r'^json/Morbilidad_Adolescente$',views.JsonM.as_view()),
    url(r'^json/Riesgo_Adolescente$',views.JsonR.as_view()),
    url(r'^json/Tamizaje_Adolescente$',views.JsonT.as_view()),
]
