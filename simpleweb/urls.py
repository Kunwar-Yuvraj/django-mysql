
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('tables/', views.tables,name='tables'),
    path('tables/delete/<int:id>', views.studentdelete, name="studentdelete"),
    path('tables/studentedit/<int:id>', views.studentedit,name='studentedit'),
    path('tables/studentupdate/', views.studentupdate, name="studentupdate"),
    path('studentadd/', views.studentadd, name="studentadd"),
    path('tables/inserted/', views.studentaddprocess, name="studentaddprocess"),

]