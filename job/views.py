from django.shortcuts import render
from rest_framework import viewsets
from.models import JobPost
from .serializers import JobPostSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class JobPostviewset(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JobPost.objects.filter(poster=user)