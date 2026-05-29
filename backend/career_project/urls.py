# This file connects URL paths to the correct app

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # All user-related endpoints (register, login, logout)
    path('api/users/', include('users.urls')),

    # All roadmap-related endpoints (create, list, update)
    path('api/roadmap/', include('roadmap.urls')),
]
