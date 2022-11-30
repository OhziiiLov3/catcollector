from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

# Temp add Ctas class


class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    def __str__(self):
        return f"{self.name}"


cats = [
    Cat('Lolo', 'tabby', 'foul little goober', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]



def index(request):
    return render(request, 'index.html', {'cats': cats})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')


def cat_index(request):
    return render(request,'cat/index.html', {'cats': cats})

