from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
    queryset = User.objects.all()
    serialized = UserSerializer(queryset,many = True)
    return Response(serialized.data)


@api_view(['POST'])
def register(request):  
    body = request.data
    serializer = UserSerializer(data=body)  # Correct usage of the UserSerializer
    if serializer.is_valid():
        serializer.save()  # Save the serialized data to the database
        return Response({'message':'User added successfully!'}, status=201)  # Return a successful response
    return Response(serializer.errors, status=400)  # Return errors if validation fails