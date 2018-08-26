from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC- Model, View, Controller

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False) #set whenever the fields are updated
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True) #set when the field is initialized

	#the difference between python2 and python3 
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id":self.id})