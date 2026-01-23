from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(default=False)

    class Meta:
        fields = ['id', 'title', 'done']
        model = Todo
        ref_name = 'ViewsetApiSerializer'
