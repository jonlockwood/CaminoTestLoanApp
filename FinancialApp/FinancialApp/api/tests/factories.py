from django.test import TestCase
from factory import DjangoModelFactory, Faker
from ..models import LoanApp

# Create your tests here.
# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/

class LoanAppFactory(DjangoModelFactory):
    lastupdated = Faker('datetime')
    RequestHeader = Faker('text')
    Business = Faker('text')
    Owners = Faker('text')
    CFApplicationData = Faker('text')

    class Meta:
        model = LoanApp