from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.projects.models import ProjectMembership


class AddMembershipSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    role = serializers.ChoiceField(choices=get_user_model().Role.choices)

    class Meta:
        model = ProjectMembership
        fields = ("email", "role")

    def validate_email(self, value):
        try:
            user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("Bunday email bazada mavjud emas.")

        return value


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = ("id", "role", "joined_at")
