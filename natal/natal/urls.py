#Standard libraries imports
from django.urls import path
#Local apps imports
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
