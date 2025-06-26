from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Notification(BaseModel):
    class NotificationType(models.TextChoices):
        TASK_ASSIGNED = "Task Assigned", _("Task Assigned")
        STATUS_CHANGED = "Status Changed", _("Status Changed")
        READY_FOR_TEST = "Ready For Test", _("Ready For Test")
        TASK_REJECTED = "Task Rejected", _("Task Rejected")
        HIGH_PRIORITY = "High Priority Task", _("High Priority Task")

    notification_type = models.CharField(_("Notification Type"), max_length=30,
                                         choices=NotificationType.choices)
    message = models.TextField(_("Message"))
    is_read = models.BooleanField(_("Is Read"), default=False)

    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notification')

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return f"{self.user_id} | {self.task_id}"


class Attachment(BaseModel):
    file = models.FileField(_("File"), upload_to='task_attachments/')

    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name='attachments')
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")

    def __str__(self):
        return f"Attachment for #{self.task_id}"
