from django.contrib import admin
from django.urls import path


# 别忘了导入 listorders 函数
from sales.views import listorders,listcustomers

urlpatterns = [

    # 添加如下的路由记录
    path('orders/', listorders),
    path('customers/', listcustomers),

]
