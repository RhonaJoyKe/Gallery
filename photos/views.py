from django.shortcuts import render,redirect
import datetime as dt
from .models import Image,Category,Location
from django.http  import HttpResponse,Http404


# Create your views here.
def welcome(request):
    return render(request,'photos/welcome.html')