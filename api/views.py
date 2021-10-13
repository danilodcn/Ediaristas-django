from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.cidades_atendimento_service import listar_diaristas_cidade
from .serializers.diaristas_cidade import DiaristaCidadeSerializer
import time
# Create your templates here.

class DiaristasCidadeList(APIView):
    def get(self, request, format=None):
        cep: str = self.request.query_params.get("cep", [])
        diaristas = listar_diaristas_cidade(cep)
        # time.sleep(10)
        serializer = DiaristaCidadeSerializer(
                    diaristas,
                    many=True,
                    context={"request": request}
        )

        return Response(serializer.data)

