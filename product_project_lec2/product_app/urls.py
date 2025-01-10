from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("product/list/", views.product_list, name="product_list"),
    path("product/detail/<str:pk>/", views.product_detail, name='product_detail'), #<> : url변수(파라미터)
    path('product/insert/', views.product_insert, name="product_insert"),
    path('product/update/<str:prdno>/', views.product_update, name='product_update'),
    path('product/delete/<str:prdno>/', views.product_delete, name='product_delete'),
    path('product/search/', views.product_search_form, name='product_search_form'),
    path('product/search/result/', views.product_searchres,name='product_search_res'),
    path('product/ajax/test/', views.ajax_test, name='ajax_test'), #ajax 연습 템플릿 요청 url
    path('product/ajax/data/', views.get_data, name='get_data'), # ajax 통한 data 요청 url
    path('product/search2/', views.product_search_form2, name='product_search_form2'),
    path('product/search/result2/', views.product_searchres2,name='product_search_res2'),    
]