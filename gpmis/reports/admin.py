from django.contrib import admin
from .models import Executions

class ExecutionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Executions, ExecutionsAdmin)
