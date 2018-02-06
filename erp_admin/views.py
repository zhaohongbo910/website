# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Mainannouncements 
from erp_admin.models import *
import json

# Create your views here.
class WebView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        return context
class Main(WebView):
    def get(self,request):
        # ctx = {}
        # ctx = 300
        ctx = Mainannouncements.objects.all()
        a = Mainannouncements.objects.all()
        print(a)
        print(ctx)
        return render(request, 'main.html', locals())
     # def post(self, request, *args, **kwargs):
     #    form = self.form_class(request.POST)
     #    if form.is_valid():
     #        # <process form cleaned data>
     #        return HttpResponseRedirect('/success/')

# class  Main(TemplateView):
#             template_name = "main.html"
#             def get(self, request):
#                 list_notice = Mainannouncements.objects.all()
#                 return render(request,self.template_name, {"list":list_notice})
            # def post(self, request, *args, **kwargs):
            #     form = self.form_class(request.POST)
            #     if form.is_valid():
            #     return render(request, self.template_name, {'form': form})

class Announcement(TemplateView):
    template_name = "announcement.html"
    def get(self, request):
        li_ld = request.GET.get("id")
        lis = Mainannouncements.objects.get(pk=li_ld)
        return render(request,self.template_name, {"content":lis})
       
class WarehouseManagement(TemplateView):
     template_name  =  "warehouse_management.html"
     def get(self,request):
         waylist = Wayout.objects.all()
         if(waylist!=""):
            return render(request,self.template_name,{"waylist":waylist})
         return render(request,self.template_name)
     def post(self,request):
          dic = {
                'out_singlenum':request.POST.get("out_single_number"),
                'out_theme':request.POST.get("out_theme"),
                'sales_invoice':request.POST.get("sales_invoice"),
                'customer_name':request.POST.get("customer_name"),
                'modules':request.POST.get("modules")
          }
          print(dic)
          Wayout.objects.create(**dic)
          waylist = Wayout.objects.all()
          return render(request,self.template_name,{"waylist":waylist})

class Stockmanagement(TemplateView):
    template_name = "stock_management.html"
    def get(self, request):
        return render(request,self.template_name, locals())
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST
            print("form"+"***********"+form["stock_num"])
            stock_num = request.POST.get("stock_num")
            print("stock_num"+stock_num)
        # if form.is_valid():
        return render(request,self.template_name, locals())
        
                       