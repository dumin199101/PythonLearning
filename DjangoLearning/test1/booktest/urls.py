from django.urls import path
from . import views

urlpatterns = [
    path('getTest1',views.getTest1),
    path('getTest2',views.getTest2),
    path('getTest3',views.getTest3),
]
