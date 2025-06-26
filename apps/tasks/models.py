from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Task(BaseModel):
    class Status(models.TextChoices):
        BACKLOG = "Backlog", _("Backlog")
        TO_DO = "To Do", _("To Do")
        IN_PROGRESS = "In Progress", _("In Progress")
        READY_FOR_TESTING = "Ready For Testing", "Ready For Testing"
        REJECTED = "Rejected", _('Rejected')

    class Priority(models.TextChoices):
        LOW = "Low", _("Low (Green)")
        MEDIUM = "Medium", _("Medium (Yellow)")
        HIGH = "High", _("High (Red)")

    title = models.CharField(_("Title"), max_length=250)
    description = models.TextField(_("Description"))
    status = models.CharField(_("Satus"), max_length=20, choices=Status.choices, default=Status.BACKLOG)
    priority = models.CharField(_("Priority"), max_length=20, choices=Priority.choices, default=Priority.LOW)

    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(get_user_model(),
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name="assigned_tasks")

    due_date = models.DateField(_("Due Date"), null=True, blank=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return f"#{self.id}-{self.title}"


class TaskHistory(BaseModel):
    task = models.ForeignKey("tasks.Task", on_delete=models.CASCADE, related_name='task_history')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(_("Action"), max_length=250)
    comment = models.TextField(_("Comment"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Task History")
        verbose_name_plural = _("Task Histories")
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp}: {self.user_id} - {self.task_id}"




