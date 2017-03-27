from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True, default=None, blank=True)
    date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)

# Create your models here.
class Document(models.Model):
    url = models.CharField(max_length=200)
    document_owner = models.ForeignKey(UserProfile, verbose_name="User", null=True, blank=False, default=None)

    def __str__ (self):
        return self.url