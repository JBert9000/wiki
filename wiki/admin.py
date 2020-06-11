from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Content


class ContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Content, ContentAdmin)
