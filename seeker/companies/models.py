"""Company Models."""
from django.urls import reverse
from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    email = models.EmailField(blank=True)
    url = models.URLField()

    class Meta:
        """Order by title."""
        ordering = ["title"]

    def __str__(self):
        """Set Title."""
        return "%s" % self.title

    def get_absolute_url(self):
        """Get Company Detail URL."""
        return reverse("company_detail", args=[str(self.slug)])
