# Register models so they appear in Django's admin panel at /admin/

from django.contrib import admin
from .models import Roadmap, TopicProgress

# This lets you view and edit roadmaps from the Django admin interface
admin.site.register(Roadmap)
admin.site.register(TopicProgress)
