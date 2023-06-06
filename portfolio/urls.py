
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('disciplinas', views.disciplinas_view, name='disciplinas'),
]
