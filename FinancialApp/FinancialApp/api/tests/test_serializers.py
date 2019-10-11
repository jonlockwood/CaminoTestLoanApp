from django.test import TestCase

from ..serializers import LoanAppSerializer
from .factories import LoanAppFactory
# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/


class CompanySerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        loanapp = LoanAppFactory()
        for field_name in [
            'lastupdated', 'RequestHeader', 'Business', 'Owners', 'CFApplicationData',
        ]:
            self.assertEqual(
                LoanAppSerializer.data[field_name],
                getattr(loanapp, field_name)
            )
