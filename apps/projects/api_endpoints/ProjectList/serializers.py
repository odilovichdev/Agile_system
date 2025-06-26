from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import Project, ProjectMembership


class ProjectListMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", 'email', 'role')


class ProjectListSerializer(serializers.ModelSerializer):
    members = ProjectListMemberSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "is_active",
            "created_at",
            "members"
        )
