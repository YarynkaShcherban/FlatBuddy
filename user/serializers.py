from rest_framework import serializers
from .models import User, UserProfile, UserHousing, UserPhoto


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ['image']


class UserProfileSerializer(serializers.ModelSerializer):

    photos = UserPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHousing
        fields = '__all__'
