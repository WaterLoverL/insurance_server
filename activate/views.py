from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Insurance, PolicyHolder
from .serializers import InsuranceSerializer, PolicyHolderSerializer, UserSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class PolicyHolderViewSet(viewsets.ModelViewSet):
    queryset = PolicyHolder.objects.all()
    serializer_class = PolicyHolderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class =  UserSerializer
