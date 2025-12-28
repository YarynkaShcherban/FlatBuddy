from ..models import UserHousing
from ..serializers import UserHousingSerializer
from .BaseView import BaseViewSet


class UserHousingViewSet(BaseViewSet):
    queryset = UserHousing.objects.all()
    serializer_class = UserHousingSerializer
