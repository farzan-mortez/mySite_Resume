from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest

def index_view(request):
    return render(request, 'website/index.html')