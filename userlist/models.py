from django.db import models


class UserList(models.Model):
    uid = models.IntegerField()
    nick = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    latest = models.CharField(max_length=30)
    identity = models.CharField(max_length=30)


# Create your models here.
