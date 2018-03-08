from django.urls import path
from . import views

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
]
