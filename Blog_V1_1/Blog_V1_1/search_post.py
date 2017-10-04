#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.decorators import csrf


def search_post2(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
