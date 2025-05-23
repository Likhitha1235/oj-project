from django.db import models

# Create your models here.
languages = [
    ("C++", "C++"),
    ("Java", "Java"),
    ("python", "python"),
]


class Submission(models.Model) :
    input_code = models.TextField()
    output_code = models.TextField()
    code = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    language = models.CharField(choices = languages)

