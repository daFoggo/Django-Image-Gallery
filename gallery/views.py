from django.views import generic #Sử dụng module generic để xử lí các yêu cầu HTTP
from django.urls import reverse_lazy #Sử dụng module reverse_lazy để quay ngược về các trang html

from .models import Category, Gallery 
from .forms import GalleryForm, CategoryForm

class Home(generic.ListView):
    model = Gallery #Sử dụng model Gallery cho lớp home
    template_name = 'home.html' #Trả về template home.html
    queryset = Gallery.objects.all() #Queryset là tập hợp các đối tượng từ cơ sở dữ liệu, trong trường hợp này là tất cả các đối tượng trong model Gallery
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None) #Từ queryset lấy ra các đối tượng là category
        if category:
            queryset = queryset.filter(category__title=category) #Lọc các đối tượng (hình ảnh) thuộc category đó
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category', None)
        context['selected_category'] = category if category else "All" #Thay đổi giá trị của từ khoá 'selected_category' trong từ điển context. Dữ liệu này được
                                                                       #dùng cho dòng 17 trong template home.html
        return context
    
class UploadImage(generic.CreateView):
    model = Gallery 
    template_name = "upload-image.html" #Trả về template upload-image.html
    form_class = GalleryForm
    success_url = reverse_lazy('home') #Quay về trang home.html sau khi upload thành công
    
class CreateCategory(generic.CreateView):
    model = Category
    template_name = "create-category.html" #Trả về template create-category.html
    form_class = CategoryForm
    success_url = reverse_lazy('upload-image') #Quay về trang upload-image.html sau khi tạo category thành công