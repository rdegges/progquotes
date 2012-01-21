from django.db import models

from caching.base import CachingManager, CachingMixin


class Quote(CachingMixin, models.Model):
    """A memorable programming quote.

    All fields are optional (except for the quote body, of course).
    """
    objects = CachingManager()

    approved = models.BooleanField(default=False)
    author = models.CharField(blank=True, max_length=255)
    body = models.TextField()
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(primary_key=True)
    source = models.TextField(blank=True)
    submitted = models.DateTimeField(editable=False)
    submitted_by = models.EmailField()
    updated = models.DateTimeField(editable=False)

    def __unicode__(self):
        return u'%s - %s' % (self.body, self.author)
