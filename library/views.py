from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
#testing
from .models import Post
from .models import Author, Genre, Book, BookInstance, Language, comment

books = [
	{
		'author': 'Lorenzo',
		'title': 'hello1',
		'content': 'heckyah',
		'date_posted': 'March 2, 2020'
	},
	{
		'author': 'Santi',
		'title': 'hello2',
		'content': 'heckyahzzz',
		'date_posted': 'March 4, 2020'
	},
]


# Create your views here.
def home(request):
	#context = {
	#	'books': Post.objects.all()
	#}
	context = {
		'books': Book.objects.all()
	}
	return render(request, 'library/home.html',context)

class BookListView(ListView):
	model = Book
	template_name = 'library/home.html'
	context_object_name = 'books'

class BookDetailView(DetailView):
	model = Book

class BookCreateView(CreateView):
	model = Book
	fields = ['title','author','summary','isbn','genre','language','call']

class CommentCreateView(CreateView):
	model = comment
	fields = ['comment']

	def form_valid(self, form):
		book = Book.objects.get(pk=self.kwargs['pk'])
		form.instance.author = self.request.user
		form.instance.book = book
		return super(CommentCreateView, self).form_valid(form)


def about(request):
	return render(request, 'library/about.html',{'title':'About'})

class BookSearchView(ListView):
	model = Book
	template_name = 'library/search.html'
	context_object_name = 'books'

#def book(request,book):
#	book = Book.objects.get(title=book)
#	comments = book
	#book = Book.objects.filter(title=book).first()
	#context = {
	#	'comments': comment.objects.all()
	#}
#	return render(request, 'library/book.html',{'book':book})
	#return HttpResponse('<h1>This is the profile page! The user is {}.</h1>'.format(book))
	