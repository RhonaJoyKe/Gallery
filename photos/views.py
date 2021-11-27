from django.shortcuts import render,redirect
import datetime as dt
from .models import Article
from django.http  import HttpResponse,Http404


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')