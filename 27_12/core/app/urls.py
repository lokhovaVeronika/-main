
from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('index/', BookListView.as_view(), name="book-list"),
    path('create/', BookCreateView.as_view(), name="book-create"),
    path('update/<int:pk>', BookUpdateView.as_view(), name="book-update"),
    path('delete/<int:pk>', BookDeleteView.as_view(), name="book-delete"),
]