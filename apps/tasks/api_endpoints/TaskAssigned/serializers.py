from django.core.mail import send_mail
from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.tasks.models import Task
from apps.projects.models import ProjectMembership


class TaskAssignedSerializer(serializers.ModelSerializer):
    developer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ['developer_id', 'id', 'title', 'description', 'status', 'priority', 'assigned_to', 'due_date']
        read_only_fields = ['id', 'title', 'description', 'assigned_to', 'status', 'priority', 'due_date']

    def validate_developer_id(self, developer_id):
        task = self.instance
        try:
            developer = get_user_model().objects.get(
                id=developer_id,
                role=get_user_model().Role.DEVELOPER
            )

            # Developer loyiha azosi ekanligini tekshirish
            if not ProjectMembership.objects.filter(
                    project=task.project,
                    user=developer
            ).exists():
                raise serializers.ValidationError("Bu developer loyiha azosi emas")
            return developer
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError(f"{developer_id} bu id bilan user topilmadi.")

    def update(self, instance, validated_data):
        developer = validated_data.get("developer_id")
        instance.assigned_to = developer
        instance.save()

        # Xabarnoma yuborish
        # send_mail(
        #     'Yangi task biriktirildi',
        #     f'Sizga "{instance.title}" taski biriktirildi. Project: {instance.project.name}',
        #     'fazliddinn.gadoyev@gmail.com',
        #     [developer.email]
        # )

        return instance
