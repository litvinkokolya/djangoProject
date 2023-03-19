from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.template.response import TemplateResponse

def index(request):
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]
    user = {"name" : "Максим", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "myApp/index.html")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
# Create your views here.
