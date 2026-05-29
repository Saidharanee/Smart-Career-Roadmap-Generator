# API endpoints for generating and managing roadmaps

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Roadmap, TopicProgress
from .serializers import RoadmapSerializer
from .generator import generate_roadmap


class GenerateRoadmapView(APIView):
    """
    POST /api/roadmap/generate/
    Body: { "career_goal": "Full Stack Developer", "skills": ["HTML", "Python"] }

    Generates a personalised roadmap and saves it to the database.
    """

    def post(self, request):
        career_goal = request.data.get('career_goal', '')
        skills_list = request.data.get('skills', [])  # List of skill strings

        # Validate that required fields are present
        if not career_goal:
            return Response({'error': 'career_goal is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Generate the roadmap using our generator function
        phases = generate_roadmap(career_goal, skills_list)

        # Save the roadmap to the database (SQL INSERT)
        roadmap = Roadmap.objects.create(
            user=request.user,
            career_goal=career_goal,
            skills_input=', '.join(skills_list),
            phases=phases,
        )

        # Return the saved roadmap as JSON
        serializer = RoadmapSerializer(roadmap)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoadmapListView(APIView):
    """
    GET /api/roadmap/list/
    Returns all roadmaps saved by the logged-in user.
    SQL equivalent: SELECT * FROM roadmap WHERE user_id = <current_user>
    """

    def get(self, request):
        # Filter roadmaps by the currently logged-in user
        roadmaps = Roadmap.objects.filter(user=request.user).order_by('-created_at')
        serializer = RoadmapSerializer(roadmaps, many=True)
        return Response(serializer.data)


class RoadmapDetailView(APIView):
    """
    GET /api/roadmap/<id>/   — view a specific roadmap
    DELETE /api/roadmap/<id>/ — delete a roadmap
    """

    def get_object(self, pk, user):
        """Helper to fetch roadmap and check ownership."""
        try:
            return Roadmap.objects.get(pk=pk, user=user)
        except Roadmap.DoesNotExist:
            return None

    def get(self, request, pk):
        roadmap = self.get_object(pk, request.user)
        if not roadmap:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RoadmapSerializer(roadmap)
        return Response(serializer.data)

    def delete(self, request, pk):
        roadmap = self.get_object(pk, request.user)
        if not roadmap:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        roadmap.delete()
        return Response({'message': 'Roadmap deleted'}, status=status.HTTP_204_NO_CONTENT)


class MarkTopicView(APIView):
    """
    POST /api/roadmap/mark-topic/
    Body: { "roadmap_id": 1, "topic_name": "HTML5", "is_completed": true }

    Marks a topic as complete or incomplete.
    """

    def post(self, request):
        roadmap_id = request.data.get('roadmap_id')
        topic_name = request.data.get('topic_name')
        is_completed = request.data.get('is_completed', True)

        # Check the roadmap exists and belongs to this user
        try:
            roadmap = Roadmap.objects.get(pk=roadmap_id, user=request.user)
        except Roadmap.DoesNotExist:
            return Response({'error': 'Roadmap not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update or create the progress record (SQL UPSERT)
        progress, created = TopicProgress.objects.update_or_create(
            roadmap=roadmap,
            topic_name=topic_name,
            defaults={'is_completed': is_completed}
        )

        return Response({
            'topic': topic_name,
            'is_completed': progress.is_completed,
        })
