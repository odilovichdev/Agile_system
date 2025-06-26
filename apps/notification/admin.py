from django.contrib import admin

from .models import Attachment, Notification


@admin.register(Notification)
class NotificationAdminModel(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentModelAdmin(admin.ModelAdmin):
    pass
