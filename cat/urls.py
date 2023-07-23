from django.urls import path

from . import views

app_name = 'cat'

urlpatterns = [
    path('', views.cat_view, name='cat_view'),
    path('blogs/', views.blog_list, name='blog'),
    path('helps/', views.cat_helps, name='helps'),
    path('search/', views.search_cats, name='search_cats'),
    path('form/<int:cat_id>/', views.customers_form, name='customers_form'),

]