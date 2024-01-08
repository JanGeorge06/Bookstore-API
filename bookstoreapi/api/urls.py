from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile),
    path('books',views.Books),
    path('books/<int:id>',views.getBook),
]