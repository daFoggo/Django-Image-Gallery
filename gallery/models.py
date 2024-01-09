from django.db import models # Lớp models giúp tạo các model trong database

class Category (models.Model): #Tạo model Category
    title = models.CharField(max_length = 150, unique = True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Gallery (models.Model): 
    category = models.ForeignKey(Category, related_name = 'images', on_delete = models.CASCADE) #Tham chiếu tên category từ model Category sang model Gallery
    image = models.ImageField(upload_to='images') # Lưu ảnh vào thư mục images
    description = models.TextField(null=True, blank=True) # Mô tả có thể để trống
    created_at = models.DateTimeField(auto_now_add = True) # Thời gian đăng ảnh

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str: # Trả về tên ảnh
        return self.image.url
    
