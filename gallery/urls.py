from django.urls import path #Sử dụng module path để định nghĩa các URL
from .views import Home, UploadImage, CreateCategory #import Home đã tạo từ views

urlpatterns = [
    path('', Home.as_view(), name='home'), #Điều hướng đến Home
    path('upload-image/', UploadImage.as_view(), name='upload-image'),  #Điều hướng đến UploadImage
    path('create-category/', CreateCategory.as_view(), name ='create-category'), #Điều hướng đến CreateCategory
]

