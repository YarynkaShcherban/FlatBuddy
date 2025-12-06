from rest_framework import viewsets, status
from rest_framework.response import Response
from blockchain.blockchain_db import blockchain


class BaseViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        instance = serializer.save()
        blockchain.add_record({
            "action": f"{self.queryset.model.__name__.upper()}_CREATED",
            "id": instance.pk,
            "data": serializer.data
        })
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        blockchain.add_record({
            "action": f"{self.queryset.model.__name__.upper()}_UPDATED",
            "id": instance.pk,
            "changes": serializer.data  
        })
        return instance

    def perform_destroy(self, instance):
        blockchain.add_record({
            "action": f"{self.queryset.model.__name__.upper()}_DELETED",
            "id": instance.pk
        })
        instance.delete()
