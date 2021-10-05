from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # django will only accept image.
    image = models.ImageField(upload_to="images")