from django.shortcuts import render
from .models import Problem_set, Problem

# Create your views here.
def home_view(request) :
    my_context = []
    for i in range(1,3) :
        problem_description = Problem_set.objects.get(pk = i)
        problem_question = Problem.objects.get(pk = i)
        my_context.append({
            "problem_name" : problem_description.problem_name,
            "problem_id" : i,
            "problem_question" : problem_question.description,
            "problem_input" : problem_question.input_problem,
            "problem_output" : problem_question.output_problem,
            "problem_rating" : problem_description.rating
        })
    return render(request,"problemset.html",{"my_context" : my_context})

def problem_view(request, problem_name1) :
    problem_description = Problem_set.objects.get(problem_name = problem_name1)
    problem_question = Problem.objects.get(pk = problem_description.pk)
    my_context = ({
        "problem_name" : problem_description.problem_name,
        "problem_id" : problem_description.pk,
        "problem_question" : problem_question.description,
        "problem_input" : problem_question.input_problem,
        "problem_output" : problem_question.output_problem,
        "problem_rating" : problem_description.rating
    })
    return render(request,"problem.html",{"my_context" : my_context}) 

