from django.db import models

# Create your models here.

class Product(models.Model):
    user_type = models.TextField()
    user_id = models.TextField()
    password1 = models.TextField()
    submit = models.BooleanField()





