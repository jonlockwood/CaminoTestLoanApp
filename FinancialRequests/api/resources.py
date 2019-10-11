from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import LoanApp

class LoanAppResource(ModelResource):

    class Meta:
        queryset = LoanApp.objects.all()
        resource_name = 'loanapp'
        authorization = Authorization()

class StatusResource(ModelResource):

    class Meta:
        queryset = LoanApp.objects.all()
        resource_name = 'status'
        authorization = Authorization()