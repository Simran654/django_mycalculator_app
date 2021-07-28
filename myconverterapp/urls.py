from django.urls import path
from . import views
urlpatterns = [
    path('',views.myconverterapp,name = 'myconverterapp'),
    #path('',views.root,name = 'root'),
    path('submitquery',views.submitquery,name='submitquery'),
    path('feedback', views.feedback, name='feedback'),
    path('home',views.home,name='home'),
]
