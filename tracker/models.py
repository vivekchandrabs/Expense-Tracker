from django.db import models

# Create your models here.

class Expense(models.Model):
	title = models.CharField(max_length=100)
	amount = models.IntegerField()
	timestamp = models.DateTimeField()
	description = models.TextField()

	def __str__(self):
		return self.title


class Income(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	amount = models.IntegerField()
	timestamp = models.DateTimeField()

	def __str__(self):
		return self.title
