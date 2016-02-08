from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list,name='product_list'),
    url(r'^detail/$', views.indexView.as_view(),name='detail'),
    url(r'^checkSign/$', views.checkSign,name='checkSign'),
    url(r'^signup/$', views.signup,name='signup'),
    url(r'^sign/$', views.signpage,name='signpage'),
    url(r'^login/$', views.loginpage,name='loginpage'),
]
