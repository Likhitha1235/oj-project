from django.db import models

# Create your models here.
class Problem_set(models.Model) :
    problem_name = models.CharField(max_length = 50, blank = True, unique = True )
    rating = models.DecimalField(max_digits = 2, decimal_places = 1)
    topics = models.TextField()

class Problem(models.Model) :
    problem_id = models.ForeignKey(Problem_set, on_delete = models.CASCADE, related_name = "problem_id")
    description = models.TextField()
    input_problem = models.CharField(max_length = 200, blank = True)
    output_problem = models.CharField(max_length = 200, blank = True)

