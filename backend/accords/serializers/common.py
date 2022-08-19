from rest_framework.serializers import ModelSerializer
from ..models import Accord

class AccordSerializer(ModelSerializer):
    class Meta:
        model = Accord
        fields = ['id', 'name']