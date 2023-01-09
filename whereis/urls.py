from django.urls import path

from . import views


app_name = 'whereis'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-location', views.add_location, name='add_location'),
    path('details/<str:user_name>', views.details, name='details'),
]