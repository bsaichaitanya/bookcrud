from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):

	name =  models.CharField(max_length=10)
	isbn =  models.CharField(max_length=10,unique=True,default=None)
	user =  models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	
	

	
	def __str__(self):
		return self.name
		
		
	def get_absolute_url(self):
		return reverse('book_update', kwargs={'pk': self.pk})
	
	
	
	
