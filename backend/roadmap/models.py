# Database models for storing roadmaps in SQL

from django.db import models
from django.contrib.auth.models import User


class Roadmap(models.Model):
    """
    Stores a generated career roadmap for a user.

    SQL table: roadmap_roadmap
    Columns: id, user_id, career_goal, skills_input, phases, created_at
    """

    # Which user this roadmap belongs to (foreign key = SQL JOIN)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roadmaps')

    # The career goal the user selected
    career_goal = models.CharField(max_length=100)

    # Comma-separated skills the user entered
    skills_input = models.TextField()

    # The generated roadmap stored as JSON text
    # Example: [{"phase": 1, "title": "Foundations", "topics": ["HTML", "CSS"]}]
    phases = models.JSONField()

    # Timestamp when the roadmap was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.career_goal}"


class TopicProgress(models.Model):
    """
    Tracks which topics the user has marked as complete.
    SQL table: roadmap_topicprogress
    """

    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='progress')
    topic_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        status = "✓" if self.is_completed else "○"
        return f"{status} {self.topic_name}"
