from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.list, name = 'list'),
    path('list/<int:id>/', views.list, name = 'list_ver'),
]