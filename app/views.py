from django.shortcuts import render

# Create your views here.
from app.models import *

def Home_info(request):
    
    return render(request,'index.html')

def Hyd_info(request):
    jobs_list=Hyd_job.objects.all()
    type='HYD'
    dict={'jobs_list':jobs_list,'type':type}
    return render(request,'hydjobs.html',dict)

def Pune_info(request):
    jobs_list=Pune_jobs.objects.all()
    type='Pune'
    dict={'jobs_list':jobs_list,'type':type}
    return render(request,'hydjobs.html',dict)

def Bang_info(request):
    jobs_list=Bang_jobs.objects.all()
    type='Bang'
    dict={'jobs_list':jobs_list,'type':type}

    
    return render(request,'hydjobs.html',dict)