from django.contrib import admin

from .models import Job, Board


# class BoardAdmin(admin.ModelAdmin):
#     list_display = ('title',)


# class JobAdmin(admin.ModelAdmin):
    # list_display = ('scrape_date',)


# admin.site.register(Board, BoardAdmin)
admin.site.register(Job)
admin.site.register(Board)
