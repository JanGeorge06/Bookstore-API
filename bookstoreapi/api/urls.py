from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile),
    path('books',views.getBooks),
    path('books/<int:id>',views.getBook),
]