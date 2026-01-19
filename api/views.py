from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from .models import Tutor,Courses
from .serializers import Tutor_profile_serializers,Courses_serializers
from rest_framework.permissions import IsAuthenticated
from .models import Tutor


class Tutor_form(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Tutor.objects.all()
    serializer_class = Tutor_profile_serializers
    
class Course_form(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = Courses_serializers
    
    def perform_create(self, serializer):
        try:
            tutor, created = Tutor.objects.get_or_create(user=self.request.user)
        except Tutor.DoesNotExist:
            raise serializer.ValidationError("You must create a tutor profile first.")
        serializer.save(instructor=tutor)
