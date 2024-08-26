# myapp/admin.py
from django.contrib import admin
from django.contrib import messages
from .models import Parser
from .tasks import run_parser

@admin.action(description='Run selected parsers manually')
def run_selected_parsers(modeladmin, request, queryset):
    for parser in queryset:
        if parser.is_active:
            run_parser.delay(parser.id)
            messages.success(request, f'Parser {parser.name} has been triggered for a manual run.')
        else:
            messages.warning(request, f'Parser {parser.name} is inactive and was not run.')

@admin.register(Parser)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule_interval', 'last_run', 'is_active')
    actions = [run_selected_parsers]
