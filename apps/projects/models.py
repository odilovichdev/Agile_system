from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Project(BaseModel):
    name = models.CharField(_("Name"), max_length=250)
    description = models.TextField(_("Description"))
    is_active = models.BooleanField(_("Is Active"), default=False)

    members = models.ManyToManyField(get_user_model(), through='ProjectMembership', null=True, blank=True)
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE,
                              verbose_name=_("Owner"),
                              related_name='project_owner')

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f"{self.name}"


class ProjectMembership(BaseModel):
    role = models.CharField(_("Role"), max_length=20, choices=get_user_model().Role.choices)
    joined_at = models.DateTimeField(_("Joined At"), auto_now_add=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_membership')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='project_membership')

    class Meta:
        verbose_name = _("Project Membership")
        verbose_name_plural = _("Project Memberships")
        unique_together = ("user", "project")

    def __str__(self):
        return f"{self.user_id | self.project_id}"
