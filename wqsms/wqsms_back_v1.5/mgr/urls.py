from django.urls import path


# 别忘了导入 listorders 函数
from mgr import customer,sign_in_out,medicine,order

urlpatterns = [

    # 添加如下的路由记录
    path('customers', customer.dispatcher),
    path('medicines', medicine.dispatcher),
    path('orders', order.dispatcher),

    path('signin',sign_in_out.signin),
    path('signout',sign_in_out.signout),


]
