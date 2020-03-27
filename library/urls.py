from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('book/<book>',views.book, name='library-book'),
]

