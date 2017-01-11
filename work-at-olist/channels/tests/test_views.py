from django.test import TestCase, RequestFactory


class ChannelViewsTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_01_channels_list(self):
		request = self.factory.get('/api/v1/channels/')
		print(request)
		print(dir(request))