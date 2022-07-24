
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.response import Response
from myapp.models import Custom_User, make_token

from myapp.serializers import CustomUserSerializer
# get_user
# create_user
# update_user


class GetUserView(ListAPIView):
    """
    API for get data of one user
    """

    def get(self, request, pk):
        try:
            user: Custom_User = Custom_User.objects.get(pk=pk)
        except:
            raise Http404
        return Response(user.to_json())


class CreateUserView(GenericAPIView):
    """
    API for Create user
    """
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["token"] = make_token()
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(UpdateAPIView):
    """
    API for update user
    """
    serializer_class = CustomUserSerializer

    def get_object(self):
        token = self.request.data.get("token")
        if token:
            try:
                instance = Custom_User.objects.get(token=token)
                return instance
            except:
                raise Http404
        return False

    def update(self, request, *args, **kwargs):
        if self.get_object():
            serializer = self.serializer_class(
                self.get_object(), data=request.data, context={"request": self.get_object()})
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["token"] = make_token()
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"token": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
