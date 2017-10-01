from django.db import models

class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=200)
	date = models.DateField()
	category = models.ForeignKey("Category")
	content = models.TextField()

	def __str__(self):
		return "%s" % (self.title, )

class Category(models.Model):
	"""docstring for Category"""
	title = models.CharField(max_length=200)

	def __str__(self):
		return "%s" % (self.title, )
		
