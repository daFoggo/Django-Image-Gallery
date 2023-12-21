from django.db import models

class Category (models.Model): #Định nghĩa model Category
    title = models.CharField(max_length = 150, unique = True) #Tiêu đề một chủ đề dài tối đa 150 ký tự và không được trùng lặp

    class Meta:
        ordering = ['title'] #Sắp xếp theo tiêu đề

    def __str__(self) -> str: #Trả về tiêu đề
        return self.title


class Gallery (models.Model): 
    category = models.ForeignKey(Category, related_name = 'images', on_delete = models.CASCADE) #Tham chiếu tên category từ model Category sang model Gallery
    image = models.ImageField(upload_to='images') #Lưu ảnh vào thư mục images
    description = models.TextField(null=True, blank=True) #Mô tả có thể để trống
    created_at = models.DateTimeField(auto_now_add = True) #Ngày tạo tự động thêm vào

    class Meta:
        ordering = ['-id'] #Sắp xếp theo id

    def __str__(self) -> str: #Trả về đường dẫn ảnh
        return self.image.url