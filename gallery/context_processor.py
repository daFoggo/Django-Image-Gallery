from .models import Category

def categories(request):
    return {"categories": Category.objects.all()} #Trả về tất cả các đối tượng trong model Category