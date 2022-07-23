from decimal import InvalidContext
from multiprocessing import context
from certifi import contents
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView,UpdateAPIView
from rest_framework import status
from rest_framework.response import  Response
from myapp.models import Custom_User

from myapp.serializers import CustomUserSerializer, UpdateCustomUserSerializer
# Create your views here.
#get_user
#create_user
#update_user


class GetUserView(ListAPIView):
    def get(self,request,pk=None):
        if pk:
            try:
                user:Custom_User = Custom_User.objects.get(pk=pk)
            except:
                raise Http404
            print(user.to_json())
            return Response(user.to_json())


class CreateUserView(GenericAPIView):
    serializer_class = CustomUserSerializer
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(UpdateAPIView):
    serializer_class = UpdateCustomUserSerializer

    def get_object(self):
        token = self.request.data.get("token")
        if token:
            try:
                instance = Custom_User.objects.get(token=token)
                return instance
            except :
                raise Http404
        else:
            return JsonResponse({"token":"Token is required"},safe=False)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), data=request.data,context={"request":self.get_object()})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

            


    