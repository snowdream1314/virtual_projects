# -*- coding: UTF-8 -*- 
#-------------------------------------
# Name: 
# Purpose: learn django
# Author:
# Date: 2015-11-19
#-------------------------------------

# from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from learn.models import smzdm_fx_item


# from learn.models import smzdm_fx
# Create your views here.
# def index(request):
#     return HttpResponse(u'你好，世界')
# 
# 
# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
# 
# def add2(request,a,b):
#     c = int(a) + int(b)
#     return HttpResponse("<a href="/add/4/5/">link</a>")
def home(request):
    return render(request, 'home.html')

def show(request):
    
    #使用paginator实现分页
    limit = 10  #限制每页显示的记录数
    value = request.GET.get('text')
#     search = {""__raw__"" : {""name"":{""in"":map(re.compile,value.split('+'))}}}
    items = smzdm_fx_item.objects.filter(name__contains=value).limit(30).order_by('_fav_count')
#     items = smzdm_fx_item.objects(**search).limit(30)
    paginator = Paginator(items, limit) #实例化一个分页对象
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1    
#     page = request.GET.get('page')  #获取页码
    try:
        items = paginator.page(page)    #获取某页对应的记录
    except PageNotAnInteger :   #如果页码不是整数
        items = paginator.page(1)   #取第一页的数据
    except EmptyPage:   #如果页码太大， 没有相应记录
        items = paginator.page(paginator.num_pages) #取最后一页的记录
        
    after_range_num = 6     #页码范围
    before_range_num = 4   
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:page+before_range_num]  
#     num = items.count()
    return render_to_response('item.html', {'items':items, 'num':paginator.count, 'page_range':page_range, 'value':value}, context_instance=RequestContext(request))

def detail(request):
    limit = 8  #限制每页显示的记录数
    value = request.GET.get('text')
    items = smzdm_fx_item.objects(name__icontains=value).limit(30)
    after_range_num = 6     #页码范围
    before_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1    
    paginator = Paginator(items, limit) #实例化一个分页对象
    try:
        items = paginator.page(page)    #获取某页对应的记录
    except PageNotAnInteger :   #如果页码不是整数
        items = paginator.page(1)   #取第一页的数据
    except EmptyPage:   #如果页码太大， 没有相应记录
        items = paginator.page(paginator.num_pages) #取最后一页的记录
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:page+before_range_num]  
    return render_to_response('item.html', {'items':items,'num':paginator.count, 'page_range':page_range, 'value':value}, context_instance=RequestContext(request))
