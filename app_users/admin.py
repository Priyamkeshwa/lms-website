from django.contrib import admin
from app_users.models import UserProfileInfo
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(UserProfileInfo)


@admin.register(UserProfileInfo)
class TopicAdmin(ImportExportModelAdmin):
    pass
