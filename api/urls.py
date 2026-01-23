from django.contrib import admin
from django.urls import path, include
from .views import Tutor_form,Course_form,Course_list,Course_pk

urlpatterns = [
    path('Tutor_register/',Tutor_form.as_view()),
    path('Course_register/',Course_form.as_view()),
    path('course_list/',Course_list.as_view()),
    path('course_pk/<int:pk>/',Course_pk.as_view()),
]