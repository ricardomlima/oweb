from django.db import models

# Create your models here.
class Document(models.Model):
    url = models.CharField(max_length=200)
    document_owner = models.ForeignKey(UserProfile, verbose_name="User")

    def __str__ (self):
        return self.url

class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    login = models.CharField(max_length=25, verbose_name="Login")
    password = models.CharField(max_length=100, verbose_name="Password")
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True, default=None, blank=True)
    date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)