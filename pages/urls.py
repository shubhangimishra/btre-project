from django.urls import path
from . import views   #. is for views and urls are on same folder import views file for btre

urlpatterns = [
    path('', views.index,name='index'),
    path('about',views.about,name='about')
]