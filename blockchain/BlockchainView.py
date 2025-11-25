from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from typing import Dict
from .blockchain import blockchain, Block

class BlockchainViewSet(viewsets.ViewSet):
    def list(self, request):
        chain_data = [
            {
                "index": block.index,
                "timestamp": block.timestamp,
                "data": block.data,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }
            for block in blockchain.chain
        ]
        return Response(chain_data)

    def retrieve(self, request, pk=None):
        try:
            block = blockchain.chain[int(pk)]
            data = {
                "index": block.index,
                "timestamp": block.timestamp,
                "data": block.data,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }
            return Response(data)
        except (IndexError, ValueError):
            return Response({"error": "Блок не знайдено"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        data = request.data.get("data")
        if not isinstance(data, dict):
            return Response({"error": "Поле 'data' має бути словником"}, status=status.HTTP_400_BAD_REQUEST)
        
        block = blockchain.add_record(data)
        response_data = {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        }
        return Response(response_data, status=status.HTTP_201_CREATED)