from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Insurance, PolicyHolder


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Insurance


class PolicyHolderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PolicyHolder


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
