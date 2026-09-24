from django.contrib import admin

# Register your models here.
from .models import Application

#this is only here to test US4 (job app tracking) with out the ability to actually update the job status (another user story)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'date_applied']
    list_editable = ['status']
    list_filter = ['status']

admin.site.register(Application, ApplicationAdmin)