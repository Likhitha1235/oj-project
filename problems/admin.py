from django.contrib import admin

# Register your models here.
from .models import Problem_set

admin.site.register(Problem_set)

from .models import Problem
admin.site.register(Problem)

