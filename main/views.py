from django.shortcuts import render
from .forms import PreRegistrationForm
# Create your views here.


def index(request):
    form = PreRegistrationForm()
    return render(request, 'main/index.html', {'form': form})
