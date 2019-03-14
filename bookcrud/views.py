
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.messages.views import SuccessMessageMixin


class BookDetail(DetailView):
	model = Book
	template_name = "book_detail.html"
	slug_field = 'isbn'
	#success_url = '/success/'
	#success_message = "%(name)s was created successfully"


class BookCreate(SuccessMessageMixin,CreateView):
	model = Book
	fields = ['name','isbn']
	success_url = reverse_lazy('book_list')
	success_message = "was created successfully"
	#messages.success(message,'Your password was updated successfully!')
	
class BookList(ListView):
	model = Book
	template_name = "book_list.html"
	
class BookUpdate(UpdateView):
	model = Book
	slug_field = 'isbn'
	fields = ['name','isbn']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('book_list')
	

class BookDelete(DeleteView):
	model = Book
	slug_field = 'isbn'
	success_url = reverse_lazy('book_list')
	