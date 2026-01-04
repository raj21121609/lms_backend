from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response

class helloview(APIView):
    def get(self, request):
        return Response({
            'message':'this is working'
        })
