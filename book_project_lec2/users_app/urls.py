from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_in2/", auth_views.LoginView.as_view(template_name="users_app/sign_in2.html"), name="sign_in2"),
    path("sign_out/", views.sign_out, name="sign_out"),

]