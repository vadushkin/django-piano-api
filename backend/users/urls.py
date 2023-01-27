from django.urls import path

from .views import GetRoutesView, LoginView, LogoutView, RegisterView, UserView

urlpatterns = [
    path("", GetRoutesView.as_view(), name="users_routes"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/", UserView.as_view(), name="user"),
]
