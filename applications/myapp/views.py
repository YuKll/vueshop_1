from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('我是博客应用页面！')