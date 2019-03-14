from django.urls import path
from .views import BookCreate,BookList,BookUpdate,BookDetail,BookDelete

urlpatterns = [
    path('', BookCreate.as_view(template_name="book_form.html"),name='book_create'),
	path('list', BookList.as_view(template_name="book_list.html"),name='book_list'),
	path('update/<slug>', BookUpdate.as_view(template_name="book_update_form.html"),name='book_update'),
	path('detail/<slug>', BookDetail.as_view(template_name="book_detail.html"),name='book_detail'),
	path('delete/<slug>', BookDelete.as_view(template_name="author_confirm_delete.html"),name='book_delete'),
	
	]