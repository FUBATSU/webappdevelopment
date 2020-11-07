from django.shortcuts import render
from .models import job

# Create your views here.
def rishub(request):
    jobs = job.objects
    return render(request,'jobs/rishub.html',{'jobs':jobs})
