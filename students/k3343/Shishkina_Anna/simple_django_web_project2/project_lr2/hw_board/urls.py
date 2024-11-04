from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('homework/', views.homework_list, name='homework_list'),
    path('submit/', views.submit_homework, name='submit_homework'),
]
