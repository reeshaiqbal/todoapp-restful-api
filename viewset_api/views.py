from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    # Only authenticated & authorized users can access API
    permission_classes = [IsAuthenticated]

    # Defined the queryset of Todo objects
    queryset = Todo.objects.all()
    # Specified the serializer class used to convert Todo instances (from json->model instance and model instance->json)
    serializer_class = TodoSerializer

    # WWill get todos of the loggedin user
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
