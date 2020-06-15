from django.db import models
from django.utils import timezone
class Mylessons(models.Model):
    name = models.CharField('наименование',max_length=100)
    school = models.CharField('организация', max_length=100)
    annotation = models.TextField('аннотация')
    moneys = models.TextField('Маржа',default='')
    data_create = models.DateTimeField(default=timezone.now)

# Create your models here.
