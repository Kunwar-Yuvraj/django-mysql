
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),

    path('tables/', views.tables,name='tables'),
    path('category/', views.categorylisting, name="categorylisting"),


    path('tables/delete/<int:id>', views.studentdelete, name="studentdelete"),
    path('category/delete/<int:id>', views.categorydelete, name="categorydelete"),



    path('tables/studentedit/<int:id>', views.studentedit,name='studentedit'),
    path('category/edit/<int:id>', views.categoryedit, name="categoryedit"),

    
    path('tables/studentupdate/', views.studentupdate, name="studentupdate"),
    path('category/update/', views.categoryupdate, name="categoryupdate"),


    path('category/create/', views.categorycreate, name="categorycreate"),
    path('/studentadd/', views.studentadd, name="studentadd"),


    path('category/inserted/', views.categoryaddprocess, name="categoryaddprocess"),
    path('tables/inserted/', views.studentaddprocess, name="studentaddprocess"),
]