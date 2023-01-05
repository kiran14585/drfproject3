from django.shortcuts import render
from testapp.serializer import profileSerializer
from testapp.models import profile
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.



class profiles(APIView):
    def post(self,request):
        serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message':'done'})
        return Response(serializer.errors)




    def get(self,request):
        data=profile.objects.all()
        serializer = profileSerializer(data,many=True)
        return Response(serializer.data)
