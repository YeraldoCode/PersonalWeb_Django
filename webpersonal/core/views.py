from django.shortcuts import render, HttpResponse # type: ignore


# Create your views here.

def home(request):
    return render(request, "core/home.html")

def contact(request):
    return render(request, "core/contact.html")



def about(request):
    return render(request, "core/about.html")   