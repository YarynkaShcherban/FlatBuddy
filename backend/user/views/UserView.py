from ..models import User
from ..serializers import UserSerializer
from .BaseView import BaseViewSet


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
