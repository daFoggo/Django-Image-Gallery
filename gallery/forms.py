from django import forms 
 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 

from .models import Category, Gallery 

# lớp forms.ModelForm giúp các lớp dưới đây kế thừa các thuộc tính của các lớp từ models và tự tạo ra các biểu mẫu theo model
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery # Tạo biểu mẫu theo model Gallery
        fields = "__all__" # Lấy toàn bộ trường của model để tạo biểu mẫu

# Tượng tự như lớp GalleryForm
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

# Lớp forms.Form giúp tạo ra các biểu mẫu không dựa trên model
class LoginForm(forms.Form):
    # Tạo các trường để nhập dữ liệu
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self): #hàm clean() kiểm tra xem username và password có hợp lệ hay không
        cleaned_data = super().clean() # Hàm clean() kiểm tra xem username và password có hợp lệ hay không
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password: # Nếu username và password hợp lệ thì bắt đầu kiểm tra
            user = authenticate(username=username, password=password) # Sử dụng hàm authenticate() kiểm tra xem username và password có hợp lệ hay không

            if user is None or not user.is_active:
                raise forms.ValidationError('Invalid username or password. Please try again.') # Nếu username hoặc password không hợp lệ thì thông báo lỗi

        return cleaned_data

# Lớp UserCreationForm giúp tạo ra các biểu mẫu đăng ký người dùng
class Signupform(UserCreationForm): #lớp Signupform kế thừa lớp UserCreationForm
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User # Xác định tạo biểu mẫu theo model User
        fields =('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True): # Hàm save() lưu dữ liệu vào database
        User = super(Signupform,self).save(commit=False) 
        User.email = self.cleaned_data['email']
        User.first_name =self.cleaned_data['first_name']
        User.last_name =self.cleaned_data['last_name']
        
        if commit: 
            User.save()
        return User
