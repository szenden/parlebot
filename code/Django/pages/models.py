from django.db import models

class test(models.Model):
	title = models.CharField(max_length=200)
	question1 = models.CharField(max_length=200)
	question2 = models.CharField(max_length=200)

class insert(models.Model):
	name = models.CharField(max_length=200)
	birth_date = models.CharField(max_length=200)
	age = models.CharField(max_length=200)




# Create your models here.
