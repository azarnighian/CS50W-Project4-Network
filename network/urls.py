
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("follow/<str:this_username>", views.follow, name="follow"),
    path("unfollow/<str:this_username>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("save_edit/<int:post_id>", views.save_edit, name="save_edit"),
    path("like/<int:post_id>/<str:l_or_u>", views.like, name="like"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
