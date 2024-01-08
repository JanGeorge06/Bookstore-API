from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    user_data = User.objects.get(pk=user.id)  # Get the specific user
    serializer = UserSerializer(user_data)  # Pass the user instance to the serializer
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBooks(request):
    
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBook(request,id):
    books = Book.objects.get(id = id)
    serializer = BookSerializer(books)
    return Response(serializer.data)




