from django.contrib import admin
from bkg.models import *
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = ('description', 'creation_date', 'type', 'status')
    list_filter =  ('creation_date', 'type', 'status')
    search_fields = ['description', 'creation_date', 'type__name', 'status__name']
    actions = ['make_published']
    @admin.action(description='Генерация отчёта')
    def make_published(self, request, queryset):
        self.message_user(request, ngettext("hte", "htes", 0) , messages.SUCCESS)


admin.site.register(Issue, IssueAdmin)
admin.site.register(IssueStatus)
admin.site.register(IssueType)