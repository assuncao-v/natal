#Standard libraries imports
from django.urls import path
#Local apps imports
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('galeria', views.galeria, name='galeria'),
    path('programacao', views.programacao, name='programacao'),
    path('sobreNovaFriburgo', views.sobreNovaFriburgo, name='sobreNovaFriburgo'),
]
