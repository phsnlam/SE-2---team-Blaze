from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup_view, name = 'signup'),
    path("login/", views.login_view, name = 'login'),
    path("logout/", views.logout_view, name = 'logout'),
    path("forgot/",views.forgot_view, name = 'forgot'),
    path("userInfo/", views.get_user_info, name = 'userInfo'),
 ]
