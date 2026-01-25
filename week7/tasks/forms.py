from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Form for creating and editing tasks."""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description (optional)',
                'rows': 4,
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    def clean_title(self):
        """Validate that title is not empty."""
        title = self.cleaned_data.get('title')
        if not title or not title.strip():
            raise forms.ValidationError('Title is required.')
        return title.strip()
