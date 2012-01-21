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

    def tearDown(self):
        Quote.objects.all().delete()
