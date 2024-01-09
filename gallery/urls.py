from django.urls import path 
from .views import Home, UploadImage, CreateCategory, SearchResultsView
from . import views
from django.contrib.auth import views as auth_views

# Các đường dẫn dưới sẽ điều hướng đến các lớp, hàm trong views.py để xử lý
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('upload-image/', UploadImage.as_view(), name='upload-image'),
    path('create-category/', CreateCategory.as_view(), name ='create-category'), 
    path('search/', SearchResultsView.as_view(), name='search_results'), 
    path('login', views.Login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('signup/',views.signup,name='SignUp')
]
