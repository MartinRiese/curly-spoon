
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('whereis.urls')),
    path('admin/', admin.site.urls),
]
