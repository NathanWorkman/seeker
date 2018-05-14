from django.views.generic import TemplateView


class AboutView(TemplateView):
    """About page."""
    template_name = 'about.html'
