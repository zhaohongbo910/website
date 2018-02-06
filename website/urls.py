"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from erp_admin.views import *
from erp_admin.views import WebView as erp_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',erp_views.as_view(
         template_name = "index.html"
        ),name="index"),
    url(r'^main/$',Main.as_view(),name="main"),
    url(r'^list4/$',erp_views.as_view(
         template_name = "list4.html"
        ),name="list4"),
    url(r'^app/$',erp_views.as_view(
         template_name = "app.html"
        ),name="app"),
    url(r'^test/$',erp_views.as_view(
         template_name = "test.html"
        ),name="test"),
    url(r'^form/$',erp_views.as_view(
         template_name = "form.html"
        ),name="form"),
    url(r'^nav/$',erp_views.as_view(
         template_name = "nav.html"
        ),name="nav"),
    url(r'^navbar/$',erp_views.as_view(
         template_name = "navbar.html"
        ),name="navbar"),
    url(r'^tab/$',erp_views.as_view(
         template_name = "tab.html"
        ),name="tab"),
    url(r'^onelevel/$',erp_views.as_view(
         template_name = "onelevel.html"
        ),name="onelevel"),
    url(r'^onelevel/$',erp_views.as_view(
         template_name = "onelevel.html"
        ),name="onelevel"),
    url(r'^table/$',erp_views.as_view(
         template_name = "table.html"
        ),name="table"),
    url(r'^warehouse_management/$',WarehouseManagement.as_view(
         template_name = "warehouse_management.html"
        ),name="warehouse_management"),
    url(r'^stock_management/$',Stockmanagement.as_view(),name="stock_management"),
    # url(r'^stock_management/$',erp_views.as_view(
    #      template_name = "stock_management.html"
    #     ),name="stock_management"),
    url(r'^organizational_management/$',erp_views.as_view(
         template_name = "organizational_management.html"
        ),name="organizational_management"),
    url(r'^training_management/$',erp_views.as_view(
         template_name = "training_management.html"
        ),name="training_management"), 
    url(r'^human_archives/$',erp_views.as_view(
         template_name = "human_archives.html"
        ),name="human_archives"),
    url(r'^position_transfer/$',erp_views.as_view(
         template_name = "position_transfer.html"
        ),name="position_transfer"), 
    url(r'^stock_management/$',erp_views.as_view(
         template_name = "stock_management.html"
        ),name="stock_management"),
    url(r'^employment_interview/$',erp_views.as_view(
         template_name = "employment_interview.html"
        ),name="employment_interview"),
    url(r'^stock_search/$',erp_views.as_view(
         template_name = "stock_search.html"
        ),name="stock_search"),
    url(r'^stock_daily/$',erp_views.as_view(
         template_name = "stock_daily.html"
        ),name="stock_daily"),  
    url(r'^stock_loss/$',erp_views.as_view(
         template_name = "stock_loss.html"
        ),name="stock_loss"),  
    url(r'^purchase_requisition/$',erp_views.as_view(
         template_name = "purchase_requisition.html"
        ),name="purchase_requisition"),     
    url(r'^financial/$',erp_views.as_view(
        template_name = "financial.html"
        ),name="financial"), 
    url(r'^announcement/$',Announcement.as_view(),name="announcement"),
    url(r'^procurement_plan/$',erp_views.as_view(
        template_name = "procurement_plan.html"
        ),name="procurement_plan"),
    url(r'^procurement_search/$',erp_views.as_view(
        template_name = "procurement_search.html"
        ),name="procurement_search"),
    url(r'^procurement_order/$',erp_views.as_view(
        template_name = "procurement_order.html"
        ),name="procurement_order"),           
    url(r'^announcement/$',Announcement.as_view(),name="announcement"), 
    url(r'^equipment/$',erp_views.as_view(
        template_name = "equipment.html"
        ),name="equipment"),     
                                 
]
