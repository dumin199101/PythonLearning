from django.urls import path,re_path
from . import views

app_name = 'booktest'

urlpatterns = [
    path('getTest1',views.getTest1),
    path('getTest2',views.getTest2),
    path('getTest3',views.getTest3),
    path('postTest1',views.postTest1),
    path('postTest2',views.postTest2),
    path('responseTest',views.responseTest),
    path('responseTest1',views.responseTest1),
    path('redirectTest1',views.redirectTest1),
    path('redirectTest2',views.redirectTest2),
    path('login',views.login),
    path('logout',views.logout),
    path('session1',views.session1),
    path('session_handle',views.session_handle),
    path('showName',views.showName),
    path('index',views.index),
    path('show/<int:id>',views.show,name='show'),
    path('extendTest',views.extendTest),
    path('csrf1',views.csrf1),
    path('csrf2',views.csrf2),
    path('staticTest',views.staticTest),
    path('exception',views.excetion),
    path('uploadImg',views.uploadImg),
    path('uploadImgHandle',views.uploadImgHandle),
    re_path('pageTest/(?P<page>\d*)',views.pageTest),
]
