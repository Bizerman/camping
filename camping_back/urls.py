"""
URL configuration for camping_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from camping_back import settings
from camping_front import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.car_campings_page_render, name='car_campings_url'),
    path('car_camping/<int:id>/', views.car_camping_page_render, name='car_camping_url'),
    path('order/<int:id>/', views.order_page_render, name='order_url'),
    path('order/<int:id>/delete/',views.del_order,name="delete_order"),
    path('car_camping/<int:el_id>/add_to_order/', views.add_to_order, name='car_add_to_order')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)