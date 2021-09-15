from datetime import datetime

from django.db import models


# Create your models here.
class Issue(models.Model):
    status = models.ForeignKey('IssueStatus', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Статус')
    type = models.ForeignKey('IssueType', on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    image_path = models.ImageField(null=True)
    description = models.TextField(null=True, verbose_name='Описание обращения')
    address = models.CharField(max_length=250)
    geo = models.CharField(max_length=300, null=True)
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    resolve_date = models.DateField(blank=True, null=True)
    resolve_image = models.ImageField(blank=True, null=True)
    resolve_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class IssueStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
