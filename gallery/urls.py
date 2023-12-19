from django.urls import path #Sử dụng module path để định nghĩa các URL
from .views import Home, UploadImage #import Home đã tạo từ views

urlpatterns = [
    path('', Home.as_view(), name='home'), #Định nghĩa URL cho Home
    path('upload-image/', UploadImage.as_view(), name ='upload-image'), 
]

