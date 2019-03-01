"""Job Models."""
from django.urls import reverse
from django.db import models
from django.utils.html import format_html
from seeker.company.models import Company


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
        ordering = ["scrape_date"]

    def __str__(self):
        """Set title."""
        return "%s" % self.title

    def get_absolute_url(self):
        """Get job detail url."""
        return reverse("job_detail", args=[str(self.pk)])

    def short_url(self):
        """Return a clickable link."""
        if self.url:
            short_url = self.url[:25] + '...'
            return format_html("<a href='{}' class='simple-button' target='_blank'>View Post</a>".format(self.url))
        else:
            return self.url
    
    def get_count(self):

        return self.objects.all().count()


class SearchTerms(models.Model):
    term = models.CharField(max_length=55)

    def __str__(self):
        return u"%s" % self.term
