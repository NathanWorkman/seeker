from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.syndication.views import Feed
from rest_framework import viewsets

from .models import Job
from .serializers import JobSerializer


class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    paginate_by = 6
    queryset = Job.objects.all().order_by('-id')


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'job_detail.html'


class SearchResultsView(ListView):
    model = Job
    template_name = 'job_search_results.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Job.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

        return queryset


class JobsFeed(Feed):
    title = "Latest Jobs"
    link = "/feed/"
    description = "Latest jobs feed"

    def items(self):
        return Job.objects.order_by('-scrape_date')[:100]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.url


class JobViewSet(viewsets.ModelViewSet):

    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
