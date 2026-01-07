from django.contrib import admin
from django.urls import path, include
from .views import Tutor_form

urlpatterns = [
    path('Tutor_register/',Tutor_form.as_view())
]