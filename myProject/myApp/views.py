from django.shortcuts import render
from django.http import *
from .forms import UserForm

def index(request):
    if request.method == "POST":
        fio = request.POST.get("fio")
        age = request.POST.get("age")
        mail = request.POST.get("mail")
        image = request.POST.get("image")
        spisok = request.POST.get("spisok")
        dateAndTime = request.POST.get("dateAndTime")
        yesOrNo = request.POST.get("yesOrNo")
        output = "<h2> ФИО: {0} </h2> <h2> Возраст: {1}</h2>" \
                 "<h2> Почта: {2} </h2> <h2> Картинка {3} </h2>" \
                 "<h2> Курс: {4} </h2> <h2> Дата: {5} </h2>"\
                 "<h1> Робот? - {6}</h1>".format(fio, age, mail, image, spisok, dateAndTime, yesOrNo)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "myApp/index.html", {"form": userform})

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
# Create your views here.
