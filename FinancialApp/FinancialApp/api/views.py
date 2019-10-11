from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import LoanApp
from .serializers import LoanAppSerializer
# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/


class LoanAppViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = LoanAppSerializer
      queryset = LoanApp.objects.all()
