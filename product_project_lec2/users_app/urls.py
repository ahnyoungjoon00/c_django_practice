from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'), # form을 장고가 제공, views의 처리함수는 직접 작성함
    path('sign_in2/', auth_views.LoginView.as_view(template_name="users_app/sign_in2.html"), name='sign_in2'),
    
    path('sign_out/', views.sign_out, name='sign_out'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up2/', views.sign_up2, name='sign_up2'),

]