from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todos
from .serializers import TodosSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def Todos_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            todo = Todos.objects.get(id=pk)
            serializer = TodosSerializer(todo)
            return Response(serializer.data)
        todo = Todos.objects.all()
        serializer = TodosSerializer(todo, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        python_data = request.data
        serializer = TodosSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Data Created Successfully !!!...', "data": serializer.data}, status=status.HTTP_201_CREATED)
        # Fixed typo here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        todo = Todos.objects.get(pk=id)
        serializer = TodosSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Complete Data Updated Successfully !!!...', "data": serializer.data}, status=status.HTTP_201_CREATED)
        # Fixed typo here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        todo = Todos.objects.get(pk=id)
        serializer = TodosSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, 'msg': 'Partial Data Updated Successfully !!!...', "data": serializer.data}, status=status.HTTP_201_CREATED)
        # Fixed typo here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        todo = Todos.objects.get(pk=id)
        todo.delete()
        return Response({"success": True, 'msg': 'Data Deleted Successfully !!!...'}, status=status.HTTP_201_CREATED)
