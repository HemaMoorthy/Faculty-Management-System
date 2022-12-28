from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allfaculty/', views.allFac, name='allFac'),
    path('addfaculty/', views.addFac, name='addFac'),
    path('newfaculty/', views.newFac, name='newFac'),
    path('delfaculty/<str:pk>/', views.delFac, name='delFac'),
    path('updatefaculty/<str:pk>/', views.updateFac, name='updateFac'),
    path('getupdate/<str:pk>/', views.getUpdate, name='getUpdate'),
    path('subjects/', views.subs, name='subs'),
    path('departments/', views.depts, name='depts'),
]
