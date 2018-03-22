# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import HeroInfo,BookInfo
from django.conf import settings
from django.core.paginator import *
import os
from .task import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache

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

#静态文件
def staticTest(request):
    return render(request,'booktest/staticTest.html')

#中间件
def excetion(request):
    a = int('abc') #此处出错
    return HttpResponse('Hello World')

#上传文件
def uploadImg(request):
    return render(request,'booktest/uploadImg.html')

def uploadImgHandle(request):
    photo = request.FILES['photo']
    #确定保存路径
    photoName = os.path.join(settings.MEDIA_ROOT,photo.name)
    with open(photoName,"wb") as pic:
        for c in photo.chunks():
            pic.write(c)
    return HttpResponse("上传成功")

#分页
def pageTest(request,page):
    if page=='':
        page = 1
    list = HeroInfo.objects.all()
    #将集合进行分页处理
    paginator = Paginator(list,3)
    #得到某页的数据
    page = paginator.page(page)
    return render(request,'booktest/pageTest.html',{'page':page})

# celery实现异步
def celeryTest(request):
    task.delay()
    return HttpResponse("OK")

# 缓存视图测试
@cache_page(300)
def cacheViewTest(request):
    return HttpResponse("Hello2")

# 缓存模板
def cacheTemplateTest(request):
    return render(request,'booktest/cacheTemplateTest.html')

# 缓存数据
def cacheDataTest(request):
    cache.set("name","lieyan",15)
    name = cache.get("name")
    return HttpResponse(name)

# 富文本编辑器
def editor(request):
    return render(request,"booktest/editor.html")