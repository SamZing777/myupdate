from datetime import datetime

from django.db import models
from accounts.models import User


class Update(models.Model):
	ISSUE = (
		('Campaign', 'CAMPAIGN'),
		('Emergency', 'EMERGENCY'),
		('Good news', 'GOOD NEWS'),
		('Ceremony', 'CEREMONY'),
		('Rumour', 'RUMOUR'),
		('Story', 'STORY')
	)

	informant = models.ForeignKey(User, on_delete=models.CASCADE)
	topic = models.CharField(max_length=50)
	matter = models.CharField(max_length=10, choices=ISSUE, default='Good news')
	description = models.TextField(default='Something is going on here', help_text="What's happening there")
	area = models.CharField(max_length=255, default='e.g: Shalom str, Fagba, Lagos, Nigeria')
	date_posted = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['date_posted']

	def __str__(self):
		return self.topic

	def get_absolute_url(self):
		return reverse('update_detail', args=str([self.id]))
