# Converts Roadmap model instances to/from JSON

from rest_framework import serializers
from .models import Roadmap, TopicProgress


class TopicProgressSerializer(serializers.ModelSerializer):
    """Serializes topic completion status."""

    class Meta:
        model = TopicProgress
        fields = ['id', 'topic_name', 'is_completed', 'completed_at']


class RoadmapSerializer(serializers.ModelSerializer):
    """
    Serializes a full roadmap, including nested progress items.
    """

    # Include nested progress data in the response
    progress = TopicProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Roadmap
        fields = ['id', 'career_goal', 'skills_input', 'phases', 'created_at', 'progress']
        read_only_fields = ['id', 'created_at', 'phases', 'progress']
