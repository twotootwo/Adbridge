from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement
from .serializer import AdvertisementSerializer
from rest_framework import status

class AdvertisementAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = AdvertisementSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        qs = Advertisement.objects.all()
        serializer = AdvertisementSerializer(qs, many=True)
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs): #update
        pk = kwargs.get('pk')
        instance = Advertisement.objects.get(id=pk)
        serializer = AdvertisementSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Advertisement.objects.get(id=pk)
        instance.delete()
        return Response({'message': 'The object has been deleted'})

