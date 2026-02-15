from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, register_view, profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView, TagListView, PostsByTagView

urlpatterns =[
    path("", home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile, name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment-update"
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<str:tag_name>/", PostsByTagView.as_view(), name="posts-by-tag"),

  
]

