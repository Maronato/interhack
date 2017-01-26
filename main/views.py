from django.shortcuts import render
from .forms import PreRegistrationForm
# Create your views here.


def index(request, referee_id=""):
    form = PreRegistrationForm(initial={'referee': referee_id})
    return render(request, 'main/index.html', {'form': form})
