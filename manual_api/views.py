from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema


# Handles APIs for listing and creating todos
class TodoListDetailedAPIs(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        # many is set to true, as a list can contain multiple todos
        serializer = TodoSerializer(todos, many=True)
        numbered_list = []
        # Giving serial number to the list for frontend display
        for index, item in enumerate(serializer.data):
            new_item = {
                'display_id': index+1,
                **item
            }
            numbered_list.append(new_item)
        # Returns the serialized list with display_id
        return Response(numbered_list)

    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Handles APIs for deleting and updating a todo
class TodoListBriefAPIs(APIView):
    def delete(self, request, id):
        try:
            # id is matched and todo object with given id is retrieved
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"message": "Todo Deleted Successfully!"}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({"message": "Todo not found!"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response({"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        # data holds content that user sent to replace the todo with
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
