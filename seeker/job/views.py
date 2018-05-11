from django.views.generic import DetailView, ListView
from .models import Job

# Create your views here.


class JobDetailView(DetailView):
    """Job Detail Views."""
    model = Job


class JobListView(ListView):
    """Job List View."""
    paginate_by = 10
    model = Job

    def get_context_data(self, *args, **kwargs):
        context = super(JobListView, self).get_context_data(*args, **kwargs)
        context['job_list'] = Job.objects.order_by('-scrape_date')
        context['job_count'] = Job.objects.all().count()
        return context
