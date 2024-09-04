from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from .models import Note
from .serializers import NoteSerializer

class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Note.DoesNotExist:
            raise NotFound(detail="Note not found", code=status.HTTP_404_NOT_FOUND)

class NoteQueryView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title:
            queryset = Note.objects.filter(title__icontains=title)
            if not queryset.exists():
                raise NotFound(detail="No notes found with the given title", code=status.HTTP_404_NOT_FOUND)
            return queryset
        return Note.objects.all()

class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Note.DoesNotExist:
            raise NotFound(detail="Note not found", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)