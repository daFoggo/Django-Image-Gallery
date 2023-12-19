from django import forms

from .models import Category, Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"