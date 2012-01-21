from datetime import datetime

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
    slug = models.SlugField()
    source = models.TextField(blank=True)
    submitted = models.DateTimeField(editable=False)
    submitted_by = models.EmailField()
    updated = models.DateTimeField(editable=False)

    def __unicode__(self):
        return u'%s - %s' % (self.body, self.author)

    def save(self, *args, **kwargs):
        """Automatically populate the ``submitted`` and ``updated`` datetime
        fields.
        """
        current_time = datetime.now()

        if not self.pk:
            self.submitted = current_time

        self.updated = current_time
        super(Quote, self).save(*args, **kwargs)
