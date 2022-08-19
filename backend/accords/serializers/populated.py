from rest_framework import serializers
from ..models import Accord
from perfumes.serializers.common import SimplestPerfumeSerializer
from perfumes.models import Perfume

class PopulatedAccordSerializer(serializers.ModelSerializer):
    perfumes = SimplestPerfumeSerializer(many=True)

    class Meta:
        model = Accord
        fields = ['id', 'name', 'perfumes']