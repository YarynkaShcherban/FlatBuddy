from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blockchain.blockchain_db import blockchain
from ..models import User
from ..serializers import UserSerializer
from .BaseView import BaseViewSet

class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer