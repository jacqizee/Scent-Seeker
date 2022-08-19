from rest_framework import serializers
from ..models import Perfume
from genders.serializers.common import GenderSerializer
from brands.serializers.common import SimpleBrandSerializer
from perfume_categories.serializers.common import PerfumeCategorySerializer
from json import dumps

class SimplestPerfumeSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Perfume
        fields = ['id', 'name', 'type', 'image']

class SimplePerfumeSerializer(SimplestPerfumeSerializer):
    gender = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()

    class Meta(SimplestPerfumeSerializer.Meta):
        model = Perfume
        fields = SimplestPerfumeSerializer.Meta.fields + ['gender', 'brand']

class DetailedPerfumeSerializer(SimplePerfumeSerializer):
    accord = serializers.StringRelatedField()
    top_notes = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    mid_notes = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    base_notes = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta(SimplePerfumeSerializer.Meta):
        fields = SimplePerfumeSerializer.Meta.fields + ['accord', 'description', 'released', 'top_notes', 'mid_notes', 'base_notes']