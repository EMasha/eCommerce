from django.conf.urls import url
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    url(r'success/', views.successView, name='success'),
    url(r'error/', views.errorView, name='error'),
    url(r'^search-results/$', views.product_query, name='search-results'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),



]