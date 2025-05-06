from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView
from .forms import NotesForm

# Create your views here.
from .models import Notes

class NoteCreateView(CreateView):
    model = Notes
   # fields = ['title', 'notes']
    success_url = '/smart/notes'
    form_class = NotesForm

class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte=10)

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes':all_notes})

##todo redirect to 404 page not found or implement session

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    
    # def detail(request, pk):
    # try:
    #     note = Notes.objects.get(pk=pk)
    # except Notes.DoesNotExist:
    #     raise Http404('Note does not exists')
    # return render(request, 'notes/notes_detail.html', {'note': note})
