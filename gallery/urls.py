from django.urls import path #Sử dụng module path để định nghĩa các URL
<<<<<<< HEAD
from .views import Home, UploadImage, CreateCategory, SearchResultsView #Import các class Home, UploadImage, CreateCategory từ file views.py
from . import views
from django.contrib.auth import views as auth_views

=======
from .views import Home, UploadImage, CreateCategory  #Import các class Home, UploadImage, CreateCategory từ file views.py
from . import views
from django.contrib.auth import views as auth_views
>>>>>>> 470f87e62d5f7de250337140662eb4b2be553a0b
urlpatterns = [
    path('', Home.as_view(), name='home'), # Đường dẫn rỗng sẽ điều hướng đến class view Home
    path('upload-image/', UploadImage.as_view(), name='upload-image'),  # Đường dẫn 'upload-image/' sẽ điều hướng đến class view UploadImage
    path('create-category/', CreateCategory.as_view(), name ='create-category'), # Đường dẫn 'create-category/' sẽ điều hướng đến class view CreateCategory
<<<<<<< HEAD
    path('search/', SearchResultsView.as_view(), name='search_results'), # Đường dẫn 'search/' sẽ điều hướng đến class view SearchResultsView
    path('login', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
=======
    path('login', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', Home.as_view(), name='index'),
>>>>>>> 470f87e62d5f7de250337140662eb4b2be553a0b
    path('signup/',views.signup,name='SignUp')
]
