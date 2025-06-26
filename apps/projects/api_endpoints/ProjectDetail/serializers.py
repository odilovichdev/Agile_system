from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.projects.models import Project


class ProjectDetailMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", 'email', 'role')


class ProjectDetailSerializer(serializers.ModelSerializer):
    members = ProjectDetailMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "created_at",
            "members"
        )
