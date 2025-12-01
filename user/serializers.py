from rest_framework import serializers
from .models import User, UserProfile, UserHousing


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHousing
        fields = '__all__'
