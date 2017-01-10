from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('importcategories olist', stdout=out)
        self.assertIn('Expected output', out.getvalue())