# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

# Import library for Command Testing
from django.core.management import call_command
from django.utils.six import StringIO

class ImportCsvTest(TestCase):

	def test_output(self):
		out = StringIO()
		call_command("importcategories a", stdout=out )
		self.assertIn("Expected output", out.getvalue())

