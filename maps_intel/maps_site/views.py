import imp
from re import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #template = loader.get_template('point/index.html')
    return render(request, 'point/index.html')