from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Mylessons(models.Model):
    name = models.CharField('наименование',max_length=100)
    school = models.CharField('организация', max_length=100)
    annotation = models.TextField('аннотация')
    moneys = models.TextField('Маржа',default='')
    data_create = models.DateTimeField(default=timezone.now)
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст', default='')
    date_create = models.DateTimeField(default=timezone.now)

# Create your models here.
