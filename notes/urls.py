from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='notes.detail'),
    path('popular-notes', views.PopularNotesListView.as_view()),
    path('notes/new',views.NoteCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='notes.delete'),
    path('notes/<int:pk>/add_like', views.add_like_view, name="notes.add_like")
]