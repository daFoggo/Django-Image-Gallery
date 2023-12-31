from django.views import generic # Sử dụng module generic để sử dụng các class view xử lí các HTTP request
from django.urls import reverse_lazy # Sử dụng module reverse_lazy để quay ngược đến các URL
from django.shortcuts import render, redirect

from django.contrib import auth, messages  # Sử dụng module messages để hiển thị thông báo
from django.contrib.auth.decorators import login_required # Sử dụng module login_required sử dụng cho các tính năng cần đăng nhập
from django.contrib.auth.models import auth  # Sử dụng module auth để xác thực người dùng

from .models import Category, Gallery
from .forms import GalleryForm, CategoryForm, LoginForm, Signupform

class Home(generic.ListView): #Class Home kế thừa class ListView từ module generic
    model = Gallery 
    template_name = 'home.html'
    queryset = Gallery.objects.all() #Lấy tất cả các đối tượng trong model Gallery

    def get_queryset(self): #Hàm get_queryset() sẽ lọc các đối tượng trong model Gallery theo category
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None)
        if category:
            queryset = queryset.filter(category__title=category)
        return queryset

    def get_context_data(self, **kwargs): #Hàm get_context_data() sẽ trả về context chứa các thông tin về category được chọn
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category', None)
        context['selected_category'] = category if category else "All"
        return context

class UploadImage(generic.CreateView): #Sử dụng model Gallery và dẫn tới template upload-image.html
    model = Gallery
    template_name = "upload-image.html"
    form_class = GalleryForm
    success_url = reverse_lazy('home')

class CreateCategory(generic.CreateView): #Sử dụng model Category và dẫn tới template create-category.html
    model = Category
    template_name = "create-category.html"
    form_class = CategoryForm
    success_url = reverse_lazy('upload-image')

class SearchResultsView(generic.ListView): #Sử dụng model Gallery và dẫn tới template search-results.html
    model = Gallery
    template_name = "search-results.html"
    
    def get_queryset(self): #Hàm get_queryset() sẽ lọc các đối tượng trong model Gallery theo category
        category = self.request.GET.get('q')
        queryset = Gallery.objects.filter(category__title__icontains=category)
        return queryset
    
    def get_context_data(self, **kwargs): #Hàm get_context_data() sẽ trả về context chứa các thông tin về category được chọn
        context = super().get_context_data(**kwargs)
        context['category'] = self.request.GET.get('q')
        return context

def Login(request): #Hàm Login sẽ xử lí các request đến trang login.html
    if request.method == "POST": # Lấy dữ liệu từ các trường nhập vào và kiểm tra
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect ('home') # Quay về trang chủ khi đăng nhập thành công
        else :
            messages.error(request,"Invalid login details") # Thông báo lỗi khi đăng nhập thất bại
            
    return render(request, 'login.html', {'form': LoginForm})

@login_required # Chỉ cho phép người dùng đăng xuất khi đã đăng nhập
def logout(request): # Tương tự Login
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('home')

def signup(request):
    form = Signupform()
    if request.method =="POST":
        form = Signupform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form':form}
    return render(request,'signup.html',context=context)
