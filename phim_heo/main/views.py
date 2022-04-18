from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateListForm
from .models import User

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)
        print('b')

        if form.is_valid():
            n = form.cleaned_data["name"]
            p = form.cleaned_data["password"]
            t = User(name=n, password=p)
            t.save()
			
            return HttpResponseRedirect("/download/")

    else:
        form = CreateListForm()
        print('a')
    return render(request, 'main/index.html', {"form": form})

def home(response):
    return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")

@csrf_exempt
def download(response):
    return render(response, 'main/download.html')