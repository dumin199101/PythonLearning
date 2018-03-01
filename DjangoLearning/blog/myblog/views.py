from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def blog(request):
    book_list = BookInfo.objects.all()
    return render(request,'myblog/index.html',{'list':book_list})