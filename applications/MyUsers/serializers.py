#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19-5-24 下午3:14
# @Author : puxu
# @File : serializers.py
# @Software: PyCharm
from rest_framework import serializers, viewsets
from MyUsers.models import UserProfile



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'name', 'email', 'gender')

# from rest_framework import serializers
#
#
# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     gender = serializers.CharField(required=True,max_length=100)
#     email = serializers.EmailField()


