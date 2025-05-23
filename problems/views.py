from django.shortcuts import render
from .models import Problem_set, Problem
import random
from django.core.cache import cache


# Create your views here.

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

def home_view(request) :
    my_context = []
    all_problems = Problem_set.objects.order_by("-pk")
    latest_problems = all_problems[:10]
    for problem_description in all_problems :
        problem_question = Problem.objects.get(pk = problem_description.pk)
        my_context.append({
            "problem_name" : problem_description.problem_name,
            "problem_id" : problem_description.pk,
            "problem_question" : problem_question.description,
            "problem_input" : problem_question.input_problem,
            "problem_output" : problem_question.output_problem,
            "problem_rating" : problem_description.rating
        }) 
    random_context = cache.get("random_problem_of_the_day")
    if not random_context :
        random_problem_des = random.choice(all_problems)
        random_problem_question =  Problem.objects.get(pk = random_problem_des.pk)
        random_context = ({
            "random_id" : random_problem_des.pk,
            "random_name" : random_problem_des.problem_name,
            "random_question" : random_problem_question.description,
            "random_input" :random_problem_question.input_problem,
            "random_output" : random_problem_question.output_problem
        })

        cache.set('random_problem_of_the_day', random_context, 86400)

    return render(request,"problemset.html",{"my_context" : my_context, "random_problem" : random_context})

