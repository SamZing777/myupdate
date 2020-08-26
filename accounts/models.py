from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	bio = models.CharField(max_length=255)

	def __str__(self):
		return self.username


class BroadcastEmail(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	subject = models.CharField(max_length=100)
	body = models.TextField()
	timeStamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.subject

	class Meta:
		verbose_name = 'Broadcast Email'
		verbose_name_plural = 'Broadcast Email'
