from django.urls import path
from .views import BookListView, BookDetailView,BookCreateView, BookSearchView, CommentCreateView, BookUpdateView, BookDeleteView, BookInstanceCreateView, BookInstanceUpdateView, BookInstanceDeleteView, AuthorListView
from.import views

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'), #path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('search/', BookSearchView.as_view(), name='library-search'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('book/<int:pk>/',BookDetailView.as_view(), name='book-detail'),#path('book/<book>',views.book, name='library-book'),
    path('book/<int:pk>/edit/',BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/',BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/addinstance/',BookInstanceCreateView.as_view(), name='bookinstance-add'),
    path('book/<int:book_id>/bookinstance/<pk>/edit/',BookInstanceUpdateView.as_view(), name='bookinstance-edit'),
    path('book/<int:book_id>/bookinstance/<pk>/delete/',BookInstanceDeleteView.as_view(), name='bookinstance-delete'),
    path('book/add/',BookCreateView.as_view(),name='book-create'),
    path('book/<int:pk>/comment/',CommentCreateView.as_view(),name='comment-create'),#path('book/comment/',CommentCreateView.as_view(),name='comment-create'),
]

