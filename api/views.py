from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from .models import Tutor,Courses
from .serializers import Tutor_profile_serializers,Courses_serializers
from rest_framework.permissions import IsAuthenticated
from .models import Tutor
from .serializers import Pk_serializers,Course_pk


class Tutor_form(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = Tutor_profile_serializers
    def perform_create(self, serializer):
        if Tutor.objects.filter(user = self.request.user).exists():
            return serializer.ValidationError("the user already exist")
        serializer.save(user = self.request.user)
    
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

class Course_list(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class= Pk_serializers
    
    def get_queryset(self):
        tutor = self.request.user.tutor
        return Courses.objects.filter(instructor=tutor)
    
class Course_pk(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = Course_pk