from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^products$', views.products, name='products'),
    url(r'^products/(?P<category_slug>[-\w+])/$', views.products, name='product_list_by_category'),
]