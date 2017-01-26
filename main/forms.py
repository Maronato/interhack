from django import forms
from registration.models import Registree


class PreRegistrationForm(forms.ModelForm):
    """PreRegistrationForm
    Base form for the pre-registration of users
    """
    referee = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Registree
        fields = ['name', 'email', 'university', 'other']
        labels = {
            'name': 'Nome',
            'university': 'Universidade',
            'other': 'Qual?'
        }
        widgets = {'other': forms.HiddenInput()}

    def set_referee(self):
        referee = self.cleaned_data['referee']
        if referee:
            try:
                referee = Registree.objects.get(id=int(referee))
                self.instance.referee = referee
                self.save()
                return True
            except:
                pass
        return False
