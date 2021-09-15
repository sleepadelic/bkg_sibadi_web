from django.contrib import admin
from bkg.models import *
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = ('description', 'creation_date', 'type', 'status', 'is_published')
    list_filter =  ('creation_date', 'type', 'status')
    search_fields = ['description', 'creation_date', 'type__name', 'status__name']
    actions = ['make_published', 'make_not_published']
    @admin.action(description='Опубликовать выбранные')
    def make_published(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, ngettext("Выбранное обращение опубликовано", f"Выбранные обращения опубликованы {len(queryset)}", len(queryset)) , messages.SUCCESS)

    @admin.action(description='Скрыть выбранные')
    def make_not_published(self, request, queryset):
        queryset.update(is_published=False)
        self.message_user(request, ngettext("Выбранное обращение скрыто",
                                            f"Выбранные обращения скрыты {len(queryset)}", len(queryset)),
                          messages.SUCCESS)


admin.site.register(Issue, IssueAdmin)
admin.site.register(IssueStatus)
admin.site.register(IssueType)