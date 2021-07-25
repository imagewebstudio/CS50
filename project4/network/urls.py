
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("update/<int:post_id>", views.update, name="update"),
    path("update/<int:post_id>/<int:page_number>", views.update, name="update"),
    path("viewuser/<int:user_id>/<int:page_number>", views.viewuser, name="viewuser"),
    path("profile", views.profile, name="profile"),
    path("public/<int:page_number>", views.public, name="public"),
    path("following/<int:page_number>", views.following, name="following"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("newpost", views.newpost, name="newpost"),

]
