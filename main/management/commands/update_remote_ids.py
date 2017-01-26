from django.core.management.base import BaseCommand
from registration.models import Registree
from registration.mailchimp_helper import update_member_remote


class Command(BaseCommand):
    help = "Updates every remote user's DJ_ID"

    def handle(self, *args, **options):

        for registree in Registree.objects.all():
            update_member_remote(registree, 'DJ_ID', str(registree.id))

        return 'Updated ' + str(len(Registree.objects.all())) + ' members successfully.'
