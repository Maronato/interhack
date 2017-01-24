from django import forms
from registration.models import Registree


class PreRegistrationForm(forms.ModelForm):
    """PreRegistrationForm
    Base form for the pre-registration of users
    """

    class Meta:
        model = Registree
        fields = ['name', 'email', 'university']
        labels = {
            'name': 'Nome',
            'university': 'Universidade',
        }
