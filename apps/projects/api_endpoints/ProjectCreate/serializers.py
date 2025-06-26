from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import Project, ProjectMembership


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "is_active",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        # Loyihani yaratish (owner avtomatik request.user dan oladi)

        project = Project.objects.create(
            **validated_data,
            owner=request.user
        )

        # Loyiha egasini ProjectMembership ga a'zo qilish (Project Owner)
        ProjectMembership.objects.create(
            project=project,
            user=request.user,
            role=get_user_model().Role.PROJECT_OWNER
        )

        return project
