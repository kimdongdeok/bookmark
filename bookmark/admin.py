from django.contrib import admin

# Register your models here.
# 관리자페이지에 모델을 등록하고 커스텀아이징
from .models import Bookmark

admin.site.register(Bookmark)

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id','site_name','url']
