from django.contrib import admin
from .models import Project

# Register your models here.
# admin.site.register(Project)
@admin.register(Project)  #changing admin and registering model
class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyInject.js",)