from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blockchain.blockchain import blockchain
from ..models import UserHousing
from ..serializers import UserHousingSerializer
from .BaseView import BaseViewSet


class UserHousingViewSet(BaseViewSet):
    queryset = UserHousing.objects.all()
    serializer_class = UserHousingSerializer
