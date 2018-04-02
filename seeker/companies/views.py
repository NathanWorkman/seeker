from django.views.generic import DetailView, ListView
from .models import Company

# Create your views here.


class CompanyDetailView(DetailView):
    """Company Detail View."""
    model = Company


class CompanyListView(ListView):
    """Companies List View."""
    paginate_by = 10
    queryset = Company.objects.all()
