from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.db.models import Q # Needed for complex DB queries (adds and/or functionality)

def index(request):
    #jobs = Job.objects.all() # Select all from DB models
    jobs = Job.objects.get(job_title__contains="Go") # Select from DB where job_title LIKE
    jobs = Job.objects.values_list('job_title', 'job_description').filter(Q(job_title__contains="Py") | Q(job_title__contains="Go")) # Select specific columns from DB WHERE job_title LIKE
    return HttpResponse(jobs)