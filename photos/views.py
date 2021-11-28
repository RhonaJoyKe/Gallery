from django.shortcuts import render,redirect
import datetime as dt
from .models import Image,Category,Location
from django.http  import HttpResponse,Http404


# Create your views here.
def welcome(request):
    photos=Image.get_all_images()
    return render(request,'photos/welcome.html',{'photos':photos})
def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})
