from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('api/',include('rest_framework.urls', namespace = 'rest_framework')),

]
