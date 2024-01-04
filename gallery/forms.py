from django import forms
 
from django.contrib.auth.forms import UserCreationForm #@Từ forms.py import UserCreationForm
from django.contrib.auth.models import User #Từ models.py import model User
from django.contrib.auth import authenticate

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

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None or not user.is_active:
                raise forms.ValidationError('Invalid username or password. Please try again.')

        return cleaned_data


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields =('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True):
        User = super(signupform,self).save(commit=False)
        User.email = self.cleaned_data['email']
        User.first_name =self.cleaned_data['first_name']
        User.last_name =self.cleaned_data['last_name']
        
        if commit:
            User.save()
        return User
