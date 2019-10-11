from rest_framework.serializers import ModelSerializer

from .models import LoanApp

# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/

class LoanAppSerializer(ModelSerializer):
    class Meta:
        model = LoanApp
        fields = (
            'lastupdated', 'RequestHeader', 'Business', 'Owners', 'CFApplicationData',
        )
        #This is absolutely where to put the check for if this is a duplicate entry, but I
        #can't figure it out with the time remaining. TODO: Find duplicates and updated the previous record here

