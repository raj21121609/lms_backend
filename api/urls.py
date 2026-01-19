from django.contrib import admin
from django.urls import path, include
from .views import Tutor_form,Course_form

urlpatterns = [
    path('Tutor_register/',Tutor_form.as_view()),
    path('Course_register/',Course_form.as_view()),
]