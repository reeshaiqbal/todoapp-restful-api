from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


# Handles APIs for listing and creating todos
class TodoListDetailedAPIs(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # req.user is the user that comes after authentication/authorization who is also logged in
        # Filters and gets todos related to the loggedin user only
        todos = Todo.objects.filter(user=request.user).order_by('-created_at')
        # many is set to true, as a list can contain multiple todos
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)


# Handles APIs for deleting and updating a todo
class TodoListBriefAPIs(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            # id is matched and todo object with given id is retrieved
            todo = Todo.objects.get(
                id=id, user=request.user)
            todo.delete()
            return Response({"message": "Todo Deleted Successfully!"}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({"message": "Todo not found!"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request, id):
        try:
            todo = Todo.objects.get(
                id=id, user=request.user)
        except Todo.DoesNotExist:
            return Response({"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        # data holds content that user sent to replace the todo with
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
