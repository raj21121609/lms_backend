from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from .models import Tutor
from .serializers import Tutor_profile_serializers
from rest_framework.permissions import IsAuthenticated


class Tutor_form(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Tutor.objects.all()
    serializer_class = Tutor_profile_serializers
