from rest_framework import serializers
from django.contrib.auth.models import User  # builtin django User model


# Inheriting from ModelSerializer, it maps model fields to serializer fields automatically
class SignupSerializer(serializers.ModelSerializer):
    # password will get accepted with request but not shown in response
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Tells Serializer which django model is connected to it
        # Specifying which fields of model the serializer should include(Serializer accepts as input/ Can include in output depending on read_only / write_only configuration.)
        # User can only interact with the fields that serializer allows
        # Defines which model fields the serializer exposes.
        fields = ['username', 'email', 'password']

    # Called when save() is ran
    # validated_data is the dict containing validated data
    def create(self, validated_data):
        user = User.objects.create_user(  # Method to save password with hashing
            username=validated_data['username'],
            # if user did not provide an email an empty string will be stored
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user   # user object(User Model instance) is returned


# serializer is used bcz we dont wanna create user or hash password, just wanna read these fields for login input validation and authentication/authorization
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
