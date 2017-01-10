from django.test import TestCase

from .factories import ChannelFactory, ChannelCategoryFactory


class ChannelTestCase(TestCase):

	def setUp(self):
		self.channel = ChannelFactory.create()

	def test_01_str(self):
		self.assertEqual(self.channel.name, str(self.channel))


class ChannelCategoryTestCase(TestCase):

	def setUp(self):
		self.category = ChannelCategoryFactory.create()

	def test_01_str(self):
		self.assertEqual(self.category.name, str(self.category))