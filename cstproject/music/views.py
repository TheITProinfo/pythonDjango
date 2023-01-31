from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_views(request):
#    return HttpResponse('<h1>this is home page of music  channel</h1>')
     return render(request, 'index.html')
