from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from knox import views as knox_views
from .models import AdvertiserProfile, InfluencerProfile, CustomUser
from .serializer import CreateUserSerializer, UpdateUserSerializer, AdvertiserProfileSerializer, \
    InfluencerProfileSerializer, LoginSerializer
from rest_framework import status


class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer

class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class= LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data, status=status.HTTP_200_OK)


class CreateAdvertiserProfileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = AdvertiserProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        qs = AdvertiserProfile.objects.all()
        serializer = AdvertiserProfileSerializer(qs, many=True)
        return Response({'data': serializer.data})

class AdvertiserProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = AdvertiserProfile.objects.get(id=pk)
        serializer = AdvertiserProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs): #update
        pk = kwargs.get('pk')
        instance = AdvertiserProfile.objects.get(id=pk)
        serializer = AdvertiserProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class CreateInfluencerProfileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = InfluencerProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs): #전체 생성된 목록 조회
        qs = InfluencerProfile.objects.all()
        serializer = InfluencerProfileSerializer(qs, many=True)
        return Response({'data': serializer.data})
class InfluencerProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = InfluencerProfile.objects.get(id=pk)
        serializer = InfluencerProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs): #update
        pk = kwargs.get('pk')
        instance = InfluencerProfile.objects.get(id=pk)
        serializer = InfluencerProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
