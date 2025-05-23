"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.views import home_view,register_view,temp_view
from problems.views import home_view as problems_home_view, problem_view
from evaluation.views import submission_view , run_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('register/',register_view),
    path('register/temp/',temp_view),   
    path('problems/',problems_home_view),
    path('problems/<str:problem_name1>/',problem_view, name = "problem"),
    path('submission/',submission_view, name = "submission"),
    path('problems/<str:problem_name1>/run/',run_view, name = "run"),
    #path('',practice_view)
]
