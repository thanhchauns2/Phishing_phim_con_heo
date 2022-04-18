from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import CreateListForm
from .models import User

# Create your views here.

def index(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            p = form.cleaned_data["password"]
            t = User(name=n, password=p)
            t.save()
			
            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateListForm()
    return render(request, 'main/index.html', {"form": form})

def home(response):
    return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")

def download(response):
    return render(response, 'main/download.html')