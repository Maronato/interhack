from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .mailchimp_helper import add_member, update_member
from main.forms import PreRegistrationForm
# Create your views here.


def pre_registration(request):
    """Pre Registation
    Allows for students to pre-register for the event
    """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PreRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Aplly it
            instance = form.save()

            try:
                instance.chimp_id = add_member(form)
                instance.save()
                messages.add_message(request, messages.SUCCESS, 'Pedido de inscrição realizado! Cheque seu email para confirmar.')
            except:
                instance.delete()
                messages.add_message(request, messages.SUCCESS, 'Oops! Não foi possível realizar sua inscrição!')

        else:
            messages.add_message(request, messages.SUCCESS, form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PreRegistrationForm()

    return render(request, 'main/index.html', {'form': form})


@csrf_exempt
def mailchimp_update(request):
    if request.method == 'POST':
        update_member(request.POST)
    return HttpResponse('')
