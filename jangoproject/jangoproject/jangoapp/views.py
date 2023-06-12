from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from . models import place,fame

# Create your views here.
def demo(request):
   obj=place.objects.all()
   fam_obj=fame.objects.all()
   return render(request,"index.html",{'result':obj,'result1':fam_obj})



