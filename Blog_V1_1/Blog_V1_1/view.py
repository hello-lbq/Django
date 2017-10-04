#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
from django.shortcuts import render


def hello(request):
    context = {}
    return render(request, 'hello.html', context)
