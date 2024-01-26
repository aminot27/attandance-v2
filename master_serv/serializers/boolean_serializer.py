from rest_framework import serializers


class BooleanResponse(serializers.Serializer):
    processed = serializers.BooleanField()
