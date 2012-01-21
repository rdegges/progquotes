from django.db import models

from caching.base import CachingManager, CachingMixin


class Quote(CachingMixin, models.Model):
    """A memorable programming quote.

    All fields are optional (except for the quote body, of course).
    """
    objects = CachingManager()
