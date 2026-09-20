from django.contrib import admin

from .models import Skill, Profile, Education, WorkExperience, Link

admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Link)