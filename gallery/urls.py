from django.urls import path #Sử dụng module path để định nghĩa các URL
from .views import Home, UploadImage, CreateCategory  #Import các class Home, UploadImage, CreateCategory từ file views.py
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Home.as_view(), name='home'), # Đường dẫn rỗng sẽ điều hướng đến class view Home
    path('upload-image/', UploadImage.as_view(), name='upload-image'),  # Đường dẫn 'upload-image/' sẽ điều hướng đến class view UploadImage
    path('create-category/', CreateCategory.as_view(), name ='create-category'), # Đường dẫn 'create-category/' sẽ điều hướng đến class view CreateCategory
    path('login', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', Home.as_view(), name='index'),
    path('signup/',views.signup,name='SignUp')
]
