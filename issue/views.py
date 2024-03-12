from rest_framework import generics, permissions
from issue.models import Issue
from issue.serializers import IssueSerializer


# Create your views here.
class IssueAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Printing created object
        print(response.data)
        return response


class IssueDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        # Printing updated object
        print(response.data)
        return response
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        # Printing deleted object
        print(instance.__dict__)
        return response