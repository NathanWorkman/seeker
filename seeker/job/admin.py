from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db.models import Count

from ..util.actions import ExportCsvMixin

from .models import Job, Board, SearchTerms

# Remove users and groups from admin
admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.register(Board)
admin.site.register(SearchTerms)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_select_related = True
    # save_on_top = True
    date_hierarchy = 'scrape_date'
    list_display = (
        "company",
        "title",
        "short_url",
        "pub_date",
        "salary",
        "location",
        "scrape_date",
        "board"
    )

    search_fields = (
        "company",
        "title",
        "city"
    )

    list_filter = [
        "board"
    ]

    actions = [
        "export_as_csv"
    ]
