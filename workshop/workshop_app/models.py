from django.db import models

class Entry(models.Model):
	lable = models.CharField(
		verbose_name='lable',
		max_length=200,
	)