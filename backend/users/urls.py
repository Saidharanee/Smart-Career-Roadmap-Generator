# Maps URL paths to the view functions

from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),  # POST — create account
    path('login/', LoginView.as_view()),         # POST — get token
    path('profile/', ProfileView.as_view()),     # GET/PUT — manage profile
]
