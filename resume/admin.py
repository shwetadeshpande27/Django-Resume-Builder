from django.contrib import admin

# Register your models here.

from .models import (
    Resume,
    Education,
    Skill,
    Project,
    Experience,
    Achievement,
)


admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Achievement)