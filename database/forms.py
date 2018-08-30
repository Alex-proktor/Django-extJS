from django import forms

from .models import Recourse


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Recourse
        fields = ('title', 'text',)
