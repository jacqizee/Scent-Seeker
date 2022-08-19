from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from .serializers.common import SimplePerfumeSerializer, DetailedPerfumeSerializer
from .models import Perfume

# Create your views here.

# Endpoint - perfumes/
# Methods - GET, POST
class ListPerfumeView(APIView):
    def get(self, _request):
        perfumes = Perfume.objects.all()
        serializer = SimplePerfumeSerializer(perfumes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = DetailedPerfumeSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Perfume successfully created!'}, status.HTTP_201_CREATED)
        except ValidationError:
            raise ValidationError(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            raise Response({'error': e}, status.HTTP_422_UNPROCESSABLE_ENTITY)

# Endpoint - perfumes/pk/
# Methods - GET, PUT, DELETE
class SinglePerfumeView(APIView):
    def get_a_perfume(self, pk):
        try:
            return Perfume.objects.get(pk=pk)
        except:
            raise NotFound({'message': 'Perfume with this id not found.'}, status.HTTP_400_BAD_REQUEST)

    def get(self, _request, pk):
        perfume = self.get_a_perfume(pk)
        serializer = DetailedPerfumeSerializer(perfume)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        perfume = self.get_a_perfume(pk)
        serializer = DetailedPerfumeSerializer(perfume, data=request.data)