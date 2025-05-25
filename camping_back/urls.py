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
    path('', views.main_page_render, name='main_page_url'),
    path('car_campings/', views.car_campings_page_render, name='car_campings_url'),
    path('tents/', views.tents_page_render, name='tents_url'),
    path('car_camping/<int:id>/', views.car_camping_page_render, name='car_camping_url'),
    path('tents/<int:id>/', views.tent_page_render, name='tent_url'),
    path('order/<int:id>/', views.order_page_render, name='order_url'),
    path('order/<int:id>/delete/',views.del_order,name="delete_order"),
    path('order/<int:id>/form/',views.finalize_order,name="form_order"),
    path('add-to-order/<str:product_type>/<int:product_id>/',views.add_to_order,name='add_to_order'),
    path('add-service-to-order/<int:service_id>/<int:car_id>/', views.add_service_to_order, name='add_service_to_order'),
    path('login/', views.login_page_render, name='login_url'),
    path('logout/', views.logout_user, name='logout_url'),
    path('sign_up/', views.sign_up_page_render, name='sign_up_page_url'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)