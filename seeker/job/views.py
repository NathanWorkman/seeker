from django.views.generic import DetailView, ListView
from .models import Job

# Create your views here.


class JobDetailView(DetailView):
    """Job Detail Views."""
    model = Job


class JobListView(ListView):
    """Job List View."""
    paginate_by = 10
    queryset = Job.objects.all()
