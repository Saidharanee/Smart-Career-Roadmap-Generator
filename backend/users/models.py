# Extends the built-in Django User with extra profile info

from django.db import models
from django.contrib.auth.models import User  # Django's built-in user model


class UserProfile(models.Model):
    """
    Stores extra info about each user.
    Linked to Django's built-in User model (one-to-one).
    """

    # Link to the built-in User (each user has exactly one profile)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # The user's career goal (e.g. "Full Stack Developer")
    career_goal = models.CharField(max_length=100, blank=True)

    # Skills the user already knows, stored as comma-separated text
    # Example: "Python, HTML, SQL"
    known_skills = models.TextField(blank=True)

    # When the profile was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
