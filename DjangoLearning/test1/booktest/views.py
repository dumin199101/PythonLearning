from django.shortcuts import render

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