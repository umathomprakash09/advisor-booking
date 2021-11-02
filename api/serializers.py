from rest_framework import serializers,fields
from .models import *
from django.contrib.auth.models import User

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self,validated_data):
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        booking_time = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
        fields = '__all__'