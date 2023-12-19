from django.shortcuts import render #Sử dụng module render để trả về các template
from django.views import generic #Sử dụng module generic để xử lí các yêu cầu HTTP

class Home(generic.TemplateView): 
    template_name = 'home.html' #Trả về template home.html