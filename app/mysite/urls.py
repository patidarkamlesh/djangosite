from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.mycontact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
]
