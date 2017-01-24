from mailchimp3 import MailChimp
from .models import Registree
from django.shortcuts import get_object_or_404
from django.conf import settings

username = settings.CHIMP_USERNAME
key = settings.CHIMP_KEY
client = MailChimp(username, key)
list_id = settings.CHIMP_LIST


def add_member(form):
    fields = {
        'NAME': form.cleaned_data['name'],
        'UNI': form.cleaned_data['university'],
        'OTHER': form.cleaned_data['other']
    }
    print(form.cleaned_data['university'])

    email = form.cleaned_data['email']

    response = client.lists.members.create(list_id, {'email_address': email, 'status': 'pending', 'merge_fields': fields, 'language': 'pt'})
    return response['unique_email_id']


def update_member(data):
    instance = get_object_or_404(Registree, chimp_id=data.get('data[id]'))
    instance.email = data.get('data[email]')
    instance.name = data.get('data[merges][NAME]')
    instance.university = data.get('data[merges][UNI]')

    instance.save()

    print('Updated, ' + instance.email)
