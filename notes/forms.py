from django import forms
from django.core.exceptions import ValidationError

from . models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = {'title', 'notes'}
        labels = {
            'notes': 'Write detailed sumary of notes here:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'notes': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('we only accept notes about Django!!')
        return title
