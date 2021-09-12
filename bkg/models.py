from datetime import datetime

from django.db import models


# Create your models here.
class Issue(models.Model):
    status = models.ForeignKey('IssueStatus', on_delete=models.SET_NULL, blank=True, null=True)
    type = models.ForeignKey('IssueType', on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    image_path = models.ImageField(null=True)
    description = models.TextField(null=True)
    address = models.CharField(max_length=250)
    geo = models.CharField(max_length=300, null=True)
    creation_date = models.DateTimeField()
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
