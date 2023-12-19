from django.views import generic #Sử dụng module generic để xử lí các yêu cầu HTTP
from django.urls import reverse_lazy

from .models import Category, Gallery
from .forms import GalleryForm, CategoryForm

class Home(generic.ListView):
    model = Gallery 
    template_name = 'home.html' #Trả về template home.html
    queryset = Gallery.objects.all() #Lấy tất cả các đối tượng trong model Gallery  
    
class UploadImage(generic.CreateView):
    model = Gallery
    template_name = "upload-image.html" #Trả về template upload-image.html
    form_class = GalleryForm
    success_url = reverse_lazy('home')
    
class CreateCategory(generic.CreateView):
    model = Category
    template_name = "create-category.html" #Trả về template create-category.html
    form_class = CategoryForm
    success_url = reverse_lazy('upload-image')