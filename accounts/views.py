from rest_framework.views import APIView
from .serializers import SignupSerializer
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema


class SignupAPI(APIView):
    # Set explicitly to override the default_permission_classes setting, in which all apis are protected by default
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SignupSerializer, responses={201: 'User registered successfully', 400: 'Bad Request'})
    def post(self, request):
        # data is sent by client, already parsed in a dict/list of dict by DRF parser
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Calls create() that we set in serializer
            return Response({'message': 'User Registered Successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: 'Login Successful!', 400: 'Username & Password required', 401: 'Invalid Credentials'})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        if not username or not password:
            return Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # authenticate() is used to check credentials, a user obj is returned if correct
        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # If user is already loggedin return the same token and if logged in for the first time create and return a new token
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "Login Successful",
                "token": token.key  # token is returned in the response
            },
            status=status.HTTP_200_OK
        )
