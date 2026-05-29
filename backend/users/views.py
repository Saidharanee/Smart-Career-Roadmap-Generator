# API views for user registration and login

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, UserProfileSerializer
from .models import UserProfile


class RegisterView(APIView):
    """
    POST /api/users/register/
    Registers a new user and returns an auth token.
    No login required to access this endpoint.
    """
    permission_classes = [permissions.AllowAny]  # Anyone can register

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generate a unique token for this user
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,       # Frontend stores this token
                'username': user.username,
                'message': 'Account created successfully!'
            }, status=status.HTTP_201_CREATED)

        # If validation fails, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    POST /api/users/login/
    Logs in a user and returns their auth token.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate() checks username + password against the database
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
            })

        return Response({'error': 'Invalid username or password'},
                        status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    """
    GET  /api/users/profile/ — view logged-in user's profile
    PUT  /api/users/profile/ — update career goal and skills
    """

    def get(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
