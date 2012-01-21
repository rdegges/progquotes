"""Application tests."""


from django.utils import unittest

from apps.quotes.models import Quote


class QuoteTestCase(unittest.TestCase):

    def setUp(self):
        self.quote = Quote.objects.create(
            author = 'Randall Degges',
            body = 'This is a test quote.'
        )

    def test_unicode_returns_unicode(self):
        self.assertIsInstance(self.quote.__unicode__(), unicode)

    def test_unicode_contains_body(self):
        self.assertTrue(self.quote.body in self.quote.__unicode__())

    def test_unicode_contains_author(self):
        self.assertTrue(self.quote.author in self.quote.__unicode__())

    def test_save_sets_submitted_time(self):
        self.assertTrue(self.quote.submitted)

    def test_save_sets_updated_time(self):
        self.assertTrue(self.quote.updated)

    def test_save_only_sets_submitted_time_on_creation(self):
        time = self.quote.submitted
        self.quote.save(force_update=True)
        self.assertEquals(time, self.quote.submitted)

    def test_save_updates_updated_time_each_save(self):
        time = self.quote.updated
        self.quote.save(force_update=True)
        self.assertNotEquals(time, self.quote.updated)

    def tearDown(self):
        Quote.objects.all().delete()
