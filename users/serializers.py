from rest_framework import serializers
from django.contrib.auth.models import User

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class Registerserializers(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only= True)
    password2 = serializers.CharField(write_only= True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("the password doesn't match")
        return attrs
        
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name = last_name,
        )
        return user
        
class Loginserializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)