from hello_django.views import ping
from django.test import TestCase
from django.test.client import Client
import pytest

class UrlsTest(TestCase):
    def test_(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'titi': 'tata!'}
        )

    def test_ping(self):
        response = self.client.get('/ping/')
        # self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'ping': 'pong!'}
        )
