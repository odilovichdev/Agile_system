from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import Project, ProjectMembership
from apps.tasks.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "status",
            "priority",
            "project",
            "due_date"
        )

    def validate(self, attrs):
        request = self.context.get("request")
        project = attrs.get('project')

        # Project Manager ni tekshirish
        if request.user.role != get_user_model().Role.PROJECT_MANAGER:
            raise serializers.ValidationError("Faqat projectga biriktirilgan Project Manager task yarata oladi.")

        # Project Manager project ga biriktirilganini tekshirish
        if not ProjectMembership.objects.filter(
                project=project,
                user=request.user,
                role=get_user_model().Role.PROJECT_MANAGER
        ).exists():
            raise serializers.ValidationError("Siz faqat o'zingiz boshqaradigan project larda task yarata olasiz.")

        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        task = Task.objects.create(
            **validated_data,
            created_by=request.user
        )
        return task
