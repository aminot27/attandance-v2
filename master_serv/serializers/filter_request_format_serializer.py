from rest_framework import serializers


class FilterRequestFormatSerializer(serializers.Serializer):
    params = serializers.DictField(child=serializers.CharField())
    values = serializers.ListField(child=serializers.CharField())
