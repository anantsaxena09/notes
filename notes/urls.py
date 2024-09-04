from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteQueryView, NoteUpdateView

urlpatterns = [
    path('notes/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/query/', NoteQueryView.as_view(), name='note-query'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
]
