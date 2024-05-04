from django.shortcuts import render
from .models import UserProfile,Todo
from rest_framework import viewsets
from .serializers import UserProfileSerializer,TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token




# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
