from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def blog(request):
    book_list = BookInfo.objects.all()
    return render(request,'myblog/index.html',{'list':book_list})

def show(request,id):
    bookinfo = BookInfo.objects.get(pk=id)
    hero_list = bookinfo.heroinfo_set.all()
    return render(request, 'myblog/show.html', {'list': hero_list})