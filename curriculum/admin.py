from django.contrib import admin
from curriculum.models import Standard, Subject, Lesson, Comment, Reply
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# admin.site.register(Standard)
# admin.site.register(Subject)
# admin.site.register(Lesson)
# admin.site.register(Comment)
# admin.site.register(Reply)


@admin.register(Standard)
@admin.register(Subject)
@admin.register(Lesson)
@admin.register(Comment)
@admin.register(Reply)
class TopicAdmin(ImportExportModelAdmin):
    pass
