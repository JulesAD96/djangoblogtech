from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name ="site"

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:slug>/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    path("contact/", views.contact, name="contact"),
    
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    
    path(
        "accounts/login/", 
        auth_views.LoginView.as_view(template_name="siteapp/registration/login.html"),
        name="login"
    ),
    
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
     
]
