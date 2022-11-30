from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name 
#         self.breed = breed
#         self.description = description
#         self.age = age
# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

# def cat_index(request):
#     return render(request,'cat_index.html', {'cats': cats})

