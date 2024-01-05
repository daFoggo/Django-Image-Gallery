from django import forms 
 
from django.contrib.auth.forms import UserCreationForm #Từ forms.py import UserCreationForm
from django.contrib.auth.models import User #Từ models.py import model User
from django.contrib.auth import authenticate #Từ models.py import hàm authenticate

from .models import Category, Gallery #Từ models.py import model Category và Gallery

#lớp forms.ModelForm giúp các lớp dưới đây kế thừa các thuộc tính của các lớp từ models và tự tạo ra các biểu mẫu theo model
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery #Tạo biểu mẫu theo model Gallery
        fields = "__all__" 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category #Tạo biểu mẫu theo model Category
        fields = "__all__"
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self): #hàm clean() kiểm tra xem username và password có hợp lệ hay không
        cleaned_data = super().clean() # xoá dữ liệu cũ nếu nhập sai dữ liệu
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password) #hàm authenticate() kiểm tra xem username và password có hợp lệ hay không

            if user is None or not user.is_active:
                raise forms.ValidationError('Invalid username or password. Please try again.') #nếu username hoặc password không hợp lệ thì thông báo lỗi

        return cleaned_data


class Signupform(UserCreationForm): #lớp Signupform kế thừa lớp UserCreationForm
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User #Tạo biểu mẫu theo model User
        fields =('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True): #hàm save() lưu thông tin người dùng
        User = super(Signupform,self).save(commit=False) 
        User.email = self.cleaned_data['email']
        User.first_name =self.cleaned_data['first_name']
        User.last_name =self.cleaned_data['last_name']
        
        if commit: 
            User.save()
        return User
