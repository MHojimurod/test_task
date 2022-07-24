from django.db import models
import hashlib
from uuid import uuid4


def md5(string: str):
    res = hashlib.md5(string)
    return str(res.hexdigest())


def make_token():
    """
    This function create  token
    """
    return md5(str(uuid4()).encode())

#User model
class Custom_User(models.Model):
    genders    =   ((1,"Male (Erkak)"),(2,"Female (Ayol)"))

    name       =   models.CharField(max_length=100,verbose_name="Ismi")
    surname    =   models.CharField(max_length=100,verbose_name="Familyasi")
    age        =   models.PositiveIntegerField(verbose_name="Yoshi")
    gender     =   models.IntegerField(choices=genders,verbose_name="Jinsi")
    created_at =   models.DateTimeField(auto_now_add=True)
    token      =   models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name
    class Meta:
        pass
    
    #This function return data on JSON
    def to_json(self):
        ctx = {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            "age":self.age,
            "gender":self.gender,
            "token":self.token
        }
        return ctx
