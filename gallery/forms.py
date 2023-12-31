from django import forms

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
    