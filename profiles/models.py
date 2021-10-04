from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # the file will not be stored in the database.
    # instead it will take the file and move it somewhere on our harddrive.
    # just the path will be stored in the database
    # django will look the data folder on the root level.
    image = models.FileField(upload_to="images")