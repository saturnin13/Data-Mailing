from django.contrib import admin

# Register your models here.
from web_app.models import ProcessedEmail


class ProcessedEmailAdmin(admin.ModelAdmin):
    list_display = ProcessedEmail.to_list_display()
    list_filter = ProcessedEmail.to_list_filter()
    search_fields = ProcessedEmail.search_fields()


admin.site.register(ProcessedEmail, ProcessedEmailAdmin)