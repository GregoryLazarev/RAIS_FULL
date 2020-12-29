from django.db import models
from django.contrib.auth.models import User

class author(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	email = models.EmailField()
	bio = models.TextField(null=True, blank = True)
	#avatar = models.ImageField(null=True)
	reg_date = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return self.user

class post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	rating = models.IntegerField(null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

class comment(models.Model):
	content = models.CharField(max_length=300)
	create_time = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(author, on_delete=models.CASCADE)
	post = models.ForeignKey(post, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.content