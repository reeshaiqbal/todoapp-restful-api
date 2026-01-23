from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    # Defined the queryset of Todo objects
    queryset = Todo.objects.all()
    # Specified the serializer class used to convert Todo instances (from json->model instance and model instance->json)
    serializer_class = TodoSerializer
