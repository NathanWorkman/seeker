from django.contrib import admin

from .models import Job, Board, SearchTerms

admin.site.register(Board)
admin.site.register(Job)
admin.site.register(SearchTerms)
