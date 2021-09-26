
from django.urls import path, include
from api.viewsets import core_viewset
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('nepseapi', core_viewset.NepseApi.as_view(), name="imagecount"),
]