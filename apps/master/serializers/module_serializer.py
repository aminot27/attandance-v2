from rest_framework import serializers

from apps.master.models.module_model import Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        exclude = ('status',)