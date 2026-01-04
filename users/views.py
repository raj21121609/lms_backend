from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import Registerserializers,Loginserializer,Userserializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Registerserializers

class LoginView(generics.GenericAPIView):
    serializer_class = Loginserializer
    def post(self,request,*args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password= password)
        if user is not None:
            token = RefreshToken.for_user(user)
            serialized_user = Userserializers(user)
            return Response({
                'user':serialized_user.data,
                'refresh':str(token),
                'access':str(token.access_token)
            })
        else:
            return Response({
                'message':'invalid user-info'
            },401)