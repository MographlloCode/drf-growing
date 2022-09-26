from django import forms

from cultivator.models import Cultivator

class CultivatorForm(forms.ModelForm):
    class Meta:
        model = Cultivator
        widgets = {
        'password': forms.PasswordInput(),
    }