from django.contrib import admin

from apps.projects.models import Project, ProjectMembership


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )


@admin.register(ProjectMembership)
class ProjectMembershipModelAdmin(admin.ModelAdmin):
    pass
