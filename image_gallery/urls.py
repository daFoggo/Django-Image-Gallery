"""
URL configuration for image_gallery project.

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
from django.conf import settings
from django.urls import path, include #Sử dụng module oath, include để định nghĩa các URL
from django.conf.urls.static import static #Dùng để định nghĩa các URL cho các file tĩnh
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')) #Định nghĩa các URL đã tạo từ trong app gallery
]

#Tự động thêm URL các file tĩnh
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
