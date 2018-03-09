# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import HeroInfo,BookInfo

# Create your views here.
def getTest1(request):
    return render(request,'booktest/getTest1.html')

def getTest2(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    context = {'a':a,'b':b,'c':c}
    return render(request,'booktest/getTest2.html',context)

def getTest3(request):
    list = request.GET.getlist('a')
    return render(request,'booktest/getTest3.html',{'list':list})

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST.get('uname')
    upassword = request.POST.get('upwd')
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upassword':upassword,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)

def responseTest(request):
    response = HttpResponse()
    response.set_cookie('name','xiaohua')
    return response

def responseTest1(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('name'):
        response.write(cookie['name'])
    return response

def redirectTest1(request):
    return HttpResponseRedirect('/booktest/redirectTest2')

def redirectTest2(request):
    return HttpResponse("这是转向来的页面")

# session 练习
#显示登陆信息
def session1(request):
    uname = request.session.get('uname','未登录')
    return render(request,'booktest/session1.html',{'uname':uname})

#显示登陆模板
def login(request):
    return render(request,'booktest/login.html')

#登陆操作
def session_handle(request):
    request.session['uname'] = request.POST['uname']
    return HttpResponseRedirect('/booktest/session1')

#删除session
def logout(request):
    del request.session['uname']
    return HttpResponseRedirect('/booktest/login')

def showName(request):
    hero = HeroInfo.objects.get(pk=1)
    context = {'hero':hero}
    return render(request,'booktest/showName.html',context)

def index(request):
    list = HeroInfo.objects.filter(isDelete=0)
    return render(request,'booktest/index.html',{'list':list})

# 反向解析
def show(request,id):
    return render(request,'booktest/show.html',{'id':id})

#模板继承
def extendTest(request):
    return render(request,'booktest/extendTest.html')

#跨站脚本攻击
def csrf1(request):
    return render(request,'booktest/csrf.html')

def csrf2(request):
    name = request.POST.get('name')
    return HttpResponse(name)