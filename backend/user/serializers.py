from rest_framework import serializers
from .models import User, UserProfile, UserHousing, UserPhoto


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "country", "city",
            "gender", "birthdate", "phone_number", "email",
            "password", "repeat_password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        repeat_password = validated_data.pop("repeat_password")
        user = User.create_user_with_password(
            validated_data, password, repeat_password)
        user.save()
        return user


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
