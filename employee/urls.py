from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view/',views.view,name='view'),
    path('add/',views.add,name='add'),
    path('remove/',views.remove,name='remove'),
    path('remove/<int:emp_id>',views.remove,name='remove'),
    path('filter/',views.filter,name='filter'),


]