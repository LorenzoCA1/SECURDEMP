from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime, timedelta
#testing
from .models import Post
from .models import Author, Genre, Book, BookInstance, Language, comment
from users.models import Activity
#testing(1)
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE


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

class LogEntryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = Activity
	template_name = 'library/logentry.html'
	context_object_name = 'activities'

	def test_func(self):
		if str(self.request.user.profile.Role) == "admin":
			return True
		return False


class AuthorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Author
	fields = ['first_name','last_name','date_of_birth','date_of_death']

	def form_valid(self, form):
		message = 'Created new author "' + form.instance.last_name + ', ' + form.instance.first_name + '"'
		updateActivity(self.request.user.profile, 'Addition', message)
		return super(AuthorCreateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Book
	fields = ['title','author','summary','isbn','genre','language','call']

	def form_valid(self, form):
		message = 'Created new book "' + form.instance.title + '"'
		updateActivity(self.request.user.profile, 'Addition', message)
		return super(BookCreateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	fields = ['title','author','summary','isbn','genre','language','call']

	def form_valid(self, form):
		message = 'Updated book "' + form.instance.title + '"'
		updateActivity(self.request.user.profile, 'Update', message)
		return super(BookUpdateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Book
	success_url = '/'

	def form_valid(self, form):
		message = 'Deleted book "' + form.instance.title + '"'
		updateActivity(self.request.user.profile, 'Deletion', message)
		return super(BookDeleteView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False

class BookInstanceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = BookInstance
	fields = ['imprint','status']
	#to pass book field to bookinstance
	def form_valid(self, form):
		book = Book.objects.get(pk=self.kwargs['pk'])
		form.instance.book = book
		message = 'Created book instance "' + form.instance.book.title + '"'
		updateActivity(self.request.user.profile, 'Addition', message)
		return super(BookInstanceCreateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False

class BookInstanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = BookInstance
	fields = ['imprint','status','due_back','borrower']

	#def form_valid(self, form):
		#book = Book.objects.get(pk=self.kwargs['bookinstance_id'])
		#form.instance.book = book
		#return super(BookInstanceUpdateView, self).form_valid(form)

	#def form_valid(self, form):
		#id = BookInstance.objects.get(pk=self.kwargs['pk'])
		#form.instance.id = id
		#return super(BookInstanceUpdateView, self).form_valid(form)
	def form_valid(self, form):
		message = 'Updated book instance "' + form.instance.book.title + '"'
		updateActivity(self.request.user.profile, 'Update', message)
		return super(BookInstanceUpdateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False		

class BookInstanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = BookInstance
	success_url = '/'

	def form_valid(self, form):
		message = 'Deleted book instance "' + form.instance.book.title + '"'
		updateActivity(self.request.user.profile, 'Deletion', message)
		return super(BookInstanceDeleteView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Book Manager":
			return True
		return False

class BookInstanceBorrowUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = BookInstance
	fields = []
	template_name = 'library/bookinstanceborrow_form.html'


	def form_valid(self, form):
		form.instance.status = 'r'
		form.instance.due_back = datetime.now() + timedelta(days=7)
		form.instance.borrower = self.request.user
		message = 'Borrowed book "' + form.instance.book.title + '" due back on ' + (form.instance.due_back.strftime("%d %B, %Y"))
		updateActivity(self.request.user.profile, 'Update', message)
		return super(BookInstanceBorrowUpdateView, self).form_valid(form)


	def test_func(self):
		if str(self.request.user.profile.Role) == "Student" or str(self.request.user.profile.Role) == "Teacher":
			return True		
		return False	

class BookInstanceReturnUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = BookInstance
	fields = []

	def form_valid(self, form):
		form.instance.status = 'a'
		form.instance.borrower = None
		form.instance.due_back = None
		message = 'Returned book "' + form.instance.book.title + '"'
		updateActivity(self.request.user.profile, 'Update', message)
		return super(BookInstanceReturnUpdateView, self).form_valid(form)


	def test_func(self):
		if str(self.request.user.profile.Role) == "Student" or str(self.request.user.profile.Role) == "Teacher":
			return True
		return False	


class CommentCreateView(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
	model = comment
	fields = ['comment']

	def form_valid(self, form):
		book = Book.objects.get(pk=self.kwargs['pk'])
		form.instance.author = self.request.user
		form.instance.book = book
		message = 'Commented "' + form.instance.comment + '" on book "' + form.instance.book.title + '"'
		updateActivity(self.request.user.profile, 'Addition', message)

		return super(CommentCreateView, self).form_valid(form)

	def test_func(self):
		if str(self.request.user.profile.Role) == "Student" or str(self.request.user.profile.Role) == "Teacher":
			return True
		return False


def about(request):
	return render(request, 'library/about.html',{'title':'About'})

class BookSearchView(ListView):
	model = Book
	template_name = 'library/search.html'
	context_object_name = 'books'

class AuthorListView(ListView):
	template_name = 'library/author.html'
	context_object_name = 'authors'
	model = Author

class AuthorDetailView(DetailView):
	model = Author

def updateActivity(user, action, content):
	newactivity = Activity(
		user = user,
		action = action,
		content = content,
	)
	newactivity.save()

#def book(request,book):
#	book = Book.objects.get(title=book)
#	comments = book
	#book = Book.objects.filter(title=book).first()
	#context = {
	#	'comments': comment.objects.all()
	#}
#	return render(request, 'library/book.html',{'book':book})
	#return HttpResponse('<h1>This is the profile page! The user is {}.</h1>'.format(book))
	