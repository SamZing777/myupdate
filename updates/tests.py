from django.test import TestCase
from django.urls import reverse

from .models import Update
from accounts.models import User

"""
class UpdateTests(TestCase):

	def setUp(self):
		self.update = Update.objects.create(
		topic='Happiness',
		matter='Good News',
		area='Ikeja, Lagos, Nigeria. Africa',
		),
		self.user = informant.objects.create(
		informant='Shawn',
		)

	def test_updates_list(self):
		self.assertEqual(f'{self.update.informant}', 'Shawn')
		self.assertEqual(f'{self.update.topic}', 'Happiness')
		self.assertEqual(f'{self.update.matter}', 'Good News')
		self.assertEqual(f'{self.update.area}', 'Ikeja, Lagos, Nigeria, Africa')

	def test_update_list_view(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Happiness')
		self.assertTemplateUsed(response, 'updates/index.html')

	def test_update_detail_view(self):
		response = self.client.get(self.update.get_absolute_url())
		no_response = self.client.get('/updates/1/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Happiness')
		self.assertTemplateUsed(response, 'updates/update_detail.html')
"""
