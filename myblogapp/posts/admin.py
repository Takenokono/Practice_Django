from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # model.pyで定義したデータベースの形を元に、新規投稿画面の登録を行う