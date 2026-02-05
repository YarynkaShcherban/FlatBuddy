from rest_framework import serializers
from ..models import UserHousing


class UserHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHousing
        fields = '__all__'