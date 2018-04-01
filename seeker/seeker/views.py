from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home Page."""
    template_name = 'home.html'


class AboutView(TemplateView):
    """About page."""
    template_name = 'about.html'
