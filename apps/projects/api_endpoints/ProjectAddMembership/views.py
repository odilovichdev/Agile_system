from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.projects.models import Project, ProjectMembership
from apps.projects.api_endpoints.ProjectAddMembership.serializers import AddMembershipSerializer, MemberSerializer


class AddMemberAPIView(CreateAPIView):
    serializer_class = AddMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        return get_object_or_404(Project, id=project_id)

    def check_permissions(self, request):
        super().check_permissions(request)
        project = self.get_object()

        if project.owner != request.user:
            raise PermissionDenied("Siz faqat o'zingiz yaratgan project ga member qo'sha olasiz.")

    def create(self, request, *args, **kwargs):
        project = self.get_object()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Foydalanuvchini email orqali topish
        user = get_user_model().objects.get(email=serializer.validated_data.get('email'))

        # Azolikni yaratish
        membership, created = ProjectMembership.objects.get_or_create(
            project=project,
            user=user,
            defaults={
                "role": serializer.validated_data.get("role")
            }
        )

        if not created:
            raise ValidationError("Bu foydalanuvchi allaqachon loyiha ishtirokchisi.")

        response_serializer = MemberSerializer(membership)

        return Response(response_serializer.data, status=201)


__all__ = [
    "AddMemberAPIView",
]
