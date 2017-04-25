from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=False, default=None)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Document(models.Model):
    url = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=False, default=None)
    category = models.ForeignKey(Category, null=False, default=None)

    def __str__ (self):
        return self.url

    class Meta:
        verbose_name = "document"
        verbose_name_plural = "documents"