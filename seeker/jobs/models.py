"""Job Models."""
from django.urls import reverse
from django.db import models

from companies.models import Company


class Board(models.Model):
    """Job board jobs were scraped from."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    url = models.URLField("URL")

    class Meta:
        """Order by title."""
        ordering = ["title"]

    def __str__(self):
        """Set title."""
        return "%s" % self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    body = models.TextField()
    url = models.URLField("URL")
    pub_date = models.TextField()
    scrape_date = models.DateTimeField()
    salary = models.TextField()
    location = models.TextField()

    class Meta:
        """Order by date published."""
        ordering = ["-scrape_date"]

    def __str__(self):
        """Set title."""
        return "%s" % self.title

    def get_absolute_url(self):
        """Get job detail url."""
        return reverse("job_detail", args=[str(self.pk)])
