from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=10)
	description = models.TextField()
