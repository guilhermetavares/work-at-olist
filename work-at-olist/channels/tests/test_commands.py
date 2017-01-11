import os
from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class ChannelCommandTestCase(TestCase):
    def test_01_fail_command_output(self):
        out = StringIO()
        call_command('importcategories', 'olist', 'file_csv', stdout=out)
        self.assertIn('File not found', out.getvalue())

    def test_02_url_command_output(self):
        out = StringIO()
        call_command(
        	'importcategories',
        	'olist',
        	'https://raw.githubusercontent.com/guilhermetavares/work-at-olist/master/work-at-olist/channels/tests/fixtures/category.csv', stdout=out)
        self.assertIn('total 23 categories found', out.getvalue())

    def test_03_file_command_output(self):
        out = StringIO()
        call_command('importcategories', 'olist', 'channels/tests/fixtures/category.csv', stdout=out)
        self.assertIn('total 23 categories found', out.getvalue())