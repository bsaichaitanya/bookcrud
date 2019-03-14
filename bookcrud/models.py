from django.db import models

# Create your models here.

class Book(models.Model):

	name =  models.CharField(max_length=10)
	isbn =  models.CharField(max_length=10,unique=True,default=None)
	
	def __str__(self):
		return self.name
		
		
	def get_absolute_url(self):
		return reverse('book_update', kwargs={'pk': self.pk})
	
	
	
	
