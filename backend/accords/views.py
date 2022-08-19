from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Accord
from .serializers import common, populated

# Create your views here.

# Endpoint - 'accords/'
# Methods - GET
class ListAccordView(APIView):
    def get(self, request):
        serializer = common.AccordSerializer(Accord.objects.all(), many=True)
        return Response(serializer.data)

class DetailedAccordView(APIView):
    def get_an_accord(self, pk):
        try:
            accord = Accord.objects.get(pk = pk)
            return accord
        except:
            raise NotFound({'error': 'Accord with this ID not found.'})

    def get(self, request, pk):
        accord = self.get_an_accord(pk)

        serializer = populated.PopulatedAccordSerializer(accord)
        return Response(serializer.data)