from user.models import UserHousing
from user.serializers import UserHousingSerializer
from .BaseView import BaseViewSet


class UserHousingViewSet(BaseViewSet):
    queryset = UserHousing.objects.all()
    serializer_class = UserHousingSerializer