from captcha import fields
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import include, path

from core.swagger import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/users/", include('apps.users.urls', namespace="users")),
    path("api/v1/projects/", include('apps.projects.urls', namespace='projects')),
    path("api/v1/tasks/", include('apps.tasks.urls', namespace='tasks')),
    path("api/v1/notification/", include('apps.notification.urls', namespace='notifications')),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
