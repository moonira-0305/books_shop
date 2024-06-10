from django.contrib import admin
from .models import Category,Books,Author


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["title","publish_time","status"]
    list_filter = ['status','created_time','publish_time']
    date_hierarchy = 'publish_time'
    search_fields = ['title','body']
    ordering = ['status','publish_time']

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ['id','full_name']