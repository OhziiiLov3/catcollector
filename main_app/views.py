from django.shortcuts import render
from django.http import HttpResponse 
from .models import Cat
# Create your views here.

# Temp add Ctas class


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
#     def __str__(self):
#         return f"{self.name}"


# cats = [
#     Cat('Lolo', 'tabby', 'foul little goober', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 7),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')


def cat_index(request):
    cats = Cat.objects.all()
    return render(request,'cats/index.html', {'cats': cats})

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request,'cats/show.html',{'cat':cat})

