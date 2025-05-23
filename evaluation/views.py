from django.shortcuts import render
from django.conf import settings
import os
import uuid
from pathlib import Path
import subprocess
from django.http import HttpResponse

# Create your views here.

def submission_view(request) :
    my_context = []
    return render(request,"problem.html", {"submit" : my_context})

def run_view(request, problem_name1) :
    if request.method == "POST" :
        input_requested = request.POST.get("input")
        code_given = request.POST.get("code")
        language_used = request.POST.get("language")
        output = run_code(language_used, code_given, input_requested)
        return render(request, "run.html", {"output" : output})

def run_code(language,code,input_data) :
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]

    for directory in directories :
        dir_path = project_path/directory 
        if not dir_path.exists() :
            dir_path.mkdir(parents = True)
    
    codes_dir = project_path/"codes"
    inputs_dir = project_path/"inputs"
    outputs_dir = project_path/"outputs"

    unique = str(uuid.uuid4())
    
    code_file_name = f"{unique}.cpp"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir/code_file_name
    input_file_path = inputs_dir/input_file_name
    output_file_path = outputs_dir/output_file_name

    with open(code_file_path, "w") as code_file :
        code_file.write(code)
    with open(input_file_path, "w") as input_file :
        input_file.write(input_data)
    with open(output_file_path,"w") as output_file :
        pass
    
    if language == "C++" :
        executable_path = codes_dir/unique
        compile_result = subprocess.run(["clang++",str(code_file_path), "-o", str(executable_path) ])
        if  compile_result.returncode == 0 :
            with open(input_file_path, "r") as input_file : 
                with open(output_file_path,"w") as output_file :
                    subprocess.run(
                        [str(executable_path)],
                        stdin = input_file,
                        stdout = output_file
                    )
    
    with open(output_file_path, "r") as output_file :
        output_data = output_file.read()

    return output_data 


