from rest_framework import serializers
from collections import OrderedDict
from myapp.models import Custom_User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ["name","surname","age","gender","token"]


