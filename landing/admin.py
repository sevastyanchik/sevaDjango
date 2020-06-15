from django.contrib import admin
from .models import Mylessons

class MyLessonAdmin(admin.ModelAdmin):
    model = Mylessons
    list_display = ('name', 'school', 'annotation', 'data_create', 'id')

admin.site.register(Mylessons, MyLessonAdmin)

# Register your models here.
