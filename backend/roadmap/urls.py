# URL routing for roadmap endpoints

from django.urls import path
from .views import GenerateRoadmapView, RoadmapListView, RoadmapDetailView, MarkTopicView

urlpatterns = [
    path('generate/', GenerateRoadmapView.as_view()),    # POST — generate new roadmap
    path('list/', RoadmapListView.as_view()),             # GET  — view all my roadmaps
    path('<int:pk>/', RoadmapDetailView.as_view()),       # GET/DELETE — single roadmap
    path('mark-topic/', MarkTopicView.as_view()),         # POST — mark topic complete
]
