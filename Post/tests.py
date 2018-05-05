from django.test import Client
import unittest
# Create your tests here.

class TestViews(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_posts_view(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code,200)
