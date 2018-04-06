from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Company, CompanyAdmin)
