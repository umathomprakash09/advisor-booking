from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

@api_view(['GET'])
def getAdvisors(request,user_id):
    try:
        user = User.objects.get(id=user_id)
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors,many=True)
        return Response({"advisors":serializer.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"Error":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addAdvisor(request):
    data = request.data
    serializer = AdvisorSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(status=status.HTTP_200_OK)


class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({
            
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "user_id":user.id
        },status=status.HTTP_200_OK)


class BookAdvisor(APIView):
    def post(self,request,user_id,advisor_id):
        try:
            user = User.objects.get(id=user_id)
            advisor = Advisor.objects.get(id=advisor_id)
            adSerializer = AdvisorSerializer(advisor)
            userSerializer = UserSerializer(user)
            request.data["user"] = user_id
            request.data["advisor"] = advisor_id
            bookSerializer = BookingSerializer(data=request.data)
            if not bookSerializer.is_valid():
                 return Response({'errors':bookSerializer.errors,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            bookSerializer.save()
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

class GetBookedCalls(APIView):
    def get(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)
            bookings = Booking.objects.all()
            advisors = []
            
            for b in bookings:
                advisor = Advisor.objects.get(id=b.advisor.id)
                advisors.append(advisor)
            serializer = BookingSerializer(bookings,many=True)
            adSerializer = AdvisorSerializer(advisors,many=True)

            return Response({"payload":adSerializer.data},status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST) 



