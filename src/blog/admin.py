from django.contrib import admin

# Register your models here.

from .models import Post # 모델을 불러오고
admin.site.register(Post) # 모델을 등록.
