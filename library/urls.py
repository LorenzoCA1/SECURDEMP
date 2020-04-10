from django.urls import path
from .views import BookListView, BookDetailView,BookCreateView, BookSearchView
from.import views

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'), #path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('search/', BookSearchView.as_view(), name='library-search'),
    path('book/<int:pk>/',BookDetailView.as_view(), name='book-detail'),#path('book/<book>',views.book, name='library-book'),
    path('book/add/',BookCreateView.as_view(),name='book-create'),
]

