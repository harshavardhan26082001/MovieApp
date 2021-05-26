from django import forms
from .models import Movies as Movies_Model

class add_movie_form(forms.ModelForm):
    class Meta:
        model = Movies_Model
        fields = '__all__'