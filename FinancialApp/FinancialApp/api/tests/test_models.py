from django.test import TestCase
from ..models import LoanApp
from .factories import LoanAppFactory

# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/

class LoanAppTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        loanApp = LoanAppFactory()
        self.assertEqual(str(loanApp), loanApp.Business)