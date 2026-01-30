from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(default=False)

    class Meta:
        fields = '__all__'
        read_only_fields = ['user']
        model = Todo
        ref_name = 'ViewsetApiSerializer'
