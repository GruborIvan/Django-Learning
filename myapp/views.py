from django.shortcuts import render
from myapp.models import Person
from django.http import HttpResponse
import json
# Create your views here.

# Hardcode radi testiranja views..
bookList = Person('Ivan','Grubor',22,'343621897');

def index(request):
    return HttpResponse('This is the main page of my application!');

# request is out request object.
def about(request):
    return HttpResponse('Hello, this is the about page!');