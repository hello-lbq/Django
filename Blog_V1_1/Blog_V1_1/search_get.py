#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
from django.shortcuts import render_to_response
from django.http import HttpResponse


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    request.coding = 'utf-8'
    if 'content' in request.GET:
        message = '你搜索的内容为：' + request.GET['content']
    else:
        message = '你提交了空的表单'
    return HttpResponse(message)
