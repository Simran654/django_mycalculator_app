from django.urls import path
from . import views
urlpatterns = [
    path('myconverterapp',views.myconverterapp,name = 'myconverterapp'),
    path('submitquery',views.submitquery,name='submitquery'),
    path('feedback', views.feedback, name='feedback'),
    path('',views.home,name='home'),
]
