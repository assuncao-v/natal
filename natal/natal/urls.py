#Standard libraries imports
from django.urls import path
#Local apps imports
from .views import *

urlpatters = [
    path('', views.index, name='home'),
]
