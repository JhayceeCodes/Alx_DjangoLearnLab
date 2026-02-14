from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, register_view

urlpatterns =[
    path("", home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register")
    # path("profile/")
]

