from django.shortcuts import render #Sử dụng module render để trả về các template
from django.views import generic #Sử dụng module generic để xử lí các yêu cầu HTTP
from django.urls import reverse_lazy

from .models import Category, Gallery
from .forms import GalleryForm
class Home(generic.TemplateView): 
    template_name = 'home.html' #Trả về template home.html

class UploadImage(generic.CreateView):
    model = Gallery
    template_name = "upload-image.html"
    form_class = GalleryForm
    success_url = reverse_lazy('home')