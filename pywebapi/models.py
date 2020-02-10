from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Users(models.Model):
	username = models.CharField(max_length= 30, unique=True, blank=False, null=False)
	password = models.CharField(max_length= 100, blank=False, null=False)

	def __str__(self):
		return self.username


class Projects(models.Model):
	name = models.CharField(max_length= 30, unique=True, blank=False, null=False)
	description = models.TextField(max_length= 200, blank=False, null=False)
	completed = models.NullBooleanField(default=False)

	def __str__(self):
		return self.name

class Actions(models.Model):
	project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
	description = models.TextField(max_length= 200, blank=False, null=False)
	note = models.TextField(max_length= 50, blank=False, null=False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


# for user in User.objects.all():
# 	Token.objects.get_or_create(user=user)