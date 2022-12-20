from django.contrib import admin
from . models import post, Category
# Register your models here.
admin.site.register(Category)

@admin.register(post)
class postAdmin(admin.ModelAdmin):
     list_display = ['id','title','body','category','authour','thumbnail_des']