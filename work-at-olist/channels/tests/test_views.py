import json

from django.test import TestCase

from rest_framework.test import APIClient

from .factories import ChannelFactory


class ChannelViewsTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()

	def test_01_channels_list(self):
		response = self.client.get('/api/v1/channels/')
		assert response.status_code == 200

	def test_01_channels_list_contents(self):
		channel = ChannelFactory.create()
		response = self.client.get('/api/v1/channels/')
		print(json.loads(response.content.decode()))
