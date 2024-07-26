
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('triggerapp.urls')),
]
#where you add configurations for urls