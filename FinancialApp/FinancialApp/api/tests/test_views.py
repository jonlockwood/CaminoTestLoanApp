from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import LoanAppFactory

# Code adapted from https://www.caktusgroup.com/blog/2019/02/01/creating-api-endpoint-django-rest-framework/

class LoanAppViewSetTestCase(TestCase):
      def setUp(self):
          self.user = UserFactory(email='testuser@example.com')
          self.user.set_password('testpassword')
          self.user.save()
          self.client.login(email=self.user.email, password='testpassword')
          self.list_url = reverse('loanapp-list')

      def get_detail_url(self, loanapp_id):
          return reverse(self.loanapp-detail, kwargs={'id': loanapp_id})

      def test_get_list(self):
          """GET the list page of Companies."""
          companies = [LoanAppFactory() for i in range(0, 3)]

          response = self.client.get(self.list_url)

          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(
              set(loanapp['id'] for loanapp in response.data['results']),
              set(loanapp.id for loanapp in companies)
          )

      def test_get_detail(self):
          """GET a detail page for a LoanApp."""
          loanapp = LoanAppFactory()
          response = self.client.get(self.get_detail_url(loanapp.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data['name'], loanapp.name)

      def test_post(self):
          """POST to create a LoanApp."""
          data = {
              'name': 'New name',
              'description': 'New description',
              'street_line_1': 'New street_line_1',
              'city': 'New City',
              'state': 'NY',
              'zipcode': '12345',
          }
          self.assertEqual(LoanApp.objects.count(), 0)
          response = self.client.post(self.list_url, data=data)
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(LoanApp.objects.count(), 1)
          loanapp = LoanApp.objects.all().first()
          for field_name in data.keys():
                self.assertEqual(getattr(loanapp, field_name), data[field_name])

      def test_put(self):
          """PUT to update a LoanApp."""
          loanapp = LoanAppFactory()
          data = {
              'name': 'New name',
              'description': 'New description',
              'street_line_1': 'New street_line_1',
              'city': 'New City',
              'state': 'NY',
              'zipcode': '12345',
          }
          response = self.client.put(
              self.get_detail_url(loanapp.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          loanapp.refresh_from_db()
          for field_name in data.keys():
              self.assertEqual(getattr(loanapp, field_name), data[field_name])

      def test_patch(self):
          """PATCH to update a LoanApp."""
          loanapp = LoanAppFactory()
          data = {'name': 'New name'}
          response = self.client.patch(
              self.get_detail_url(loanapp.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          loanapp.refresh_from_db()
          self.assertEqual(loanapp.name, data['name'])

      def test_delete(self):
          """DELETEing is not implemented."""
          loanapp = LoanAppFactory()
          response = self.client.delete(self.get_detail_url(loanapp.id))
          self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)