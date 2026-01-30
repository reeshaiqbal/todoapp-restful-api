from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    # Setting done to false in serializer, as DRF don't project default to false in swagger UI, due to django/swagger behaviour
    done = serializers.BooleanField(default=False)

    class Meta:
        # Setting which fields the serializer should include, user can only interact with the fields ser allows
        fields = '__all__'
        read_only_fields = ['user']
        model = Todo
        # To prevent swagger conflicts I gave it a unique reference name, as this project has 2 apps under same name serializers
        ref_name = "ManualApiSerializer"
