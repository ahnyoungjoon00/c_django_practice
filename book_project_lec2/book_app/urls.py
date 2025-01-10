from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/list/',views.book_list,name='book_list'), #http://127.0.0.1:8000/book/list
    path('book/detail/<str:bookno>/', views.book_detail, name='book_detail'), #http://127.0.0.1:8000/book/detail/2 - 2값은 view로 전달
    path('book/insert/',views.book_insert, name='book_insert'),
    path('book/update/<str:bookno>/', views.book_update, name='book_update'),
    path('book/delete/<str:bookno>/', views.book_delete, name='book_delete'),
    path('book/search_form_a/', views.book_search_form_a, name='book_search_form_a'),
    path('book/search_a/', views.book_search_a, name='book_search_a'),
]