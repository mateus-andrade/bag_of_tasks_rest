from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, pk=None):
        task = Task.objects.get(state='AVAILABLE')
        serializer = TaskSerializer(task)
        task.delete()

        return Response(serializer)
