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


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Books(request):
    if request.method == 'POST':
         body = request.data
         serializer = BookSerializer(data = body)
         if serializer.is_valid():
            serializer.save()  # Save the serialized data to the database
         return Response({'message':'Book added successfully!'}, status=201)
    else:
        if 'price' in request.GET:
            price = request.GET['price']
            books = Book.objects.filter(price__lte=price)
            serializer = BookSerializer(books, many = True)
            return Response(serializer.data)
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)



@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def RetrieveUpdateBook(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Book updated successfully!")
        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)