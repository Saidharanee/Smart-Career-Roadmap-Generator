# Serializers convert Python objects ↔ JSON for the API

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles user registration.
    Takes username, email, and password from the request.
    """

    password = serializers.CharField(write_only=True)  # Password won't appear in responses

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """Create the user and automatically create their profile."""
        # create_user handles password hashing automatically
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        # Create a blank profile for the new user
        UserProfile.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Handles reading and updating a user's profile data.
    """

    class Meta:
        model = UserProfile
        fields = ['career_goal', 'known_skills', 'created_at']
        read_only_fields = ['created_at']
