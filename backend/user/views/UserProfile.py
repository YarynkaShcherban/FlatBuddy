from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blockchain.blockchain_db import blockchain
from ..models import UserProfile, UserPhoto
from ..serializers import UserProfileSerializer
from .BaseView import BaseViewSet


class UserProfileViewSet(BaseViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        photos = request.FILES.getlist('photos')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        for photo in photos:
            UserPhoto.objects.create(user_profile=profile, image=photo)
        profile = self.perform_create(serializer)
        return Response(UserProfileSerializer(profile).data)

    def update(self, request, *args, **kwargs):
        photos = request.FILES.getlist('photos')
        partial = kwargs.pop('partial', False)

        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        for photo in photos:
            UserPhoto.objects.create(user_profile=profile, image=photo)
        profile = self.perform_update(serializer)
        return Response(UserProfileSerializer(profile).data)