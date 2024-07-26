
from django.contrib import admin
from django.urls import path
from triggerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('payment/', views.payment,name='payment'),
    path('information/',views.information,name='information'),
]
