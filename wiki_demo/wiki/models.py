from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Content(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='wiki_pics')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(excluded_fields=['title', 'content',
                                                 'image', 'date_posted'])

    def __str__(self):
        return self.title


def get_absolute_url(self):
    return reverse("content:wiki-details", kwargs={"id": self.id})
