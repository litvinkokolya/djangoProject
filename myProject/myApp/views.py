from django.shortcuts import render
from django.http import *
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2> Пользователь </h2> <h3> Имя: {0} Возраст: {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "myApp/index.html", {"form": userform})

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
# Create your views here.
