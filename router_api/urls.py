from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #path('', index),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('router-details/', retrieveRouterDetails, name="router-details"),
    path('create-router/', InsertRouterDetails, name="create-router"),
    path('update-router/', UpdateRouterDetails, name="update-router"),
    path('delete-router/', DeleteRouterDetails, name="delete-router"),
    path('InsertRouterDetails/',InsertRouterDetails, name="InsertRouterDetails"),
    path('retrieveRouterDetailsbyIPrange/',retrieveRouterDetailsbyIPrange, name="retrieveRouterDetailsbyIPrange"),
]

urlpatterns = format_suffix_patterns(urlpatterns)