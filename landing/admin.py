from django.contrib import admin
from .models import Mylessons,Blog

class MyLessonAdmin(admin.ModelAdmin):
    model = Mylessons
    list_display = ('name', 'school', 'annotation', 'data_create', 'id')
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('author','text','date_create')
admin.site.register(Mylessons, MyLessonAdmin)
admin.site.register(Blog, BlogAdmin)

# Register your models here.
