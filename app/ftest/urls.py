from django.urls import path

from . import views

app_name = 'ftest'
urlpatterns = [

    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:postid>/delete', views.delpost, name='delete'),
    path('<int:postid>/edit', views.editpost, name='edit'),
]
