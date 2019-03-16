
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin








class BookDetail(LoginRequiredMixin,DetailView):
	model = Book
	template_name = "book_detail.html"
	slug_field = 'isbn'
	login_url = '/accounts/login/'
	#success_url = '/success/'
	#success_message = "%(name)s was created successfully"


class BookCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
	model = Book
	fields = ['name','isbn']
	print(fields)
	print(type(fields))
	login_url = '/accounts/login/'
	success_url = reverse_lazy('book_list')
	#entry_list = list(Book.objects.all()
	message = "%(name)s was created sucessfully"
	
	success_message = message
	#messages.success(message,'Your password was updated successfully!')
	
class BookList(LoginRequiredMixin,ListView):
	model = Book
	template_name = "book_list.html"
	login_url = '/accounts/login/'
	
class BookUpdate(LoginRequiredMixin,UpdateView):
	model = Book
	slug_field = 'isbn'
	fields = ['name','isbn']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('book_list')
	login_url = '/accounts/login/'
	

class BookDelete(LoginRequiredMixin,DeleteView):
	model = Book
	slug_field = 'isbn'
	success_url = reverse_lazy('book_list')
	login_url = '/accounts/login/'
	