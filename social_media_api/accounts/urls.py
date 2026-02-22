from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserViewSet

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("follow/<int:user_id>/", UserViewSet.as_view({'post': 'follow'})),
    path("unfollow/<int:user_id>/", UserViewSet.as_view({'post': 'unfollow'})),
]