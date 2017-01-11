import json
import uuid

from django.test import TestCase

from rest_framework.test import APIClient

from .factories import ChannelFactory, ChannelCategoryFactory


class ChannelViewsTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()

	def to_json(self, response):
		return json.loads(response.content.decode())

	def test_01_channels_list(self):
		response = self.client.get('/api/v1/channels/')
		self.assertEqual(response.status_code, 200)

	def test_02_channels_list_contents(self):
		channel = ChannelFactory.create()
		response = self.client.get('/api/v1/channels/')
		self.assertEqual(self.to_json(response).get('count'), 1)

	def test_03_not_found_channels_detail_contents(self):
		response = self.client.get('/api/v1/channels/{0}/'.format(uuid.uuid4()))
		self.assertEqual(response.status_code, 404)

	def test_04_channels_detail_contents(self):
		channel = ChannelFactory.create()
		response = self.client.get('/api/v1/channels/{0}/'.format(channel.uuid))
		self.assertEqual(self.to_json(response).get('name'), channel.name)
		parent = ChannelCategoryFactory.create(channel=channel)
		children = ChannelCategoryFactory.create(channel=channel, parent=parent)
		grandchildren = ChannelCategoryFactory.create(channel=channel, parent=children)
		response = self.client.get('/api/v1/channels/{0}/'.format(channel.uuid))
		self.assertEqual(len(self.to_json(response).get('categories_tree')), 1)

	def test_05_not_found_category_detail(self):
		response = self.client.get('/api/v1/channels/{0}/'.format(uuid.uuid4()))
		self.assertEqual(response.status_code, 404)

	def test_06_category_detail(self):
		category = ChannelCategoryFactory.create()
		response = self.client.get('/api/v1/category/{0}/'.format(category.uuid))
		self.assertEqual(response.status_code, 200)