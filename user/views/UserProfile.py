from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blockchain import blockchain
from ..models import UserProfile
from ..serializers import UserProfileSerializer
from .BaseView import BaseViewSet

class UserProfileViewSet(BaseViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer