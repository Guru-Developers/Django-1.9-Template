from rest_framework import serializers
from apps.sample.models import Sample

class SampleSerializer(serializers.ModelSerializer):
    """
    Used to serialize information based on REST endpoint.
    """
    class Meta:
        model = Sample
        fields = ('id', 'title', 'img_src',)
