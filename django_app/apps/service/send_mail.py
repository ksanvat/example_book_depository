from django.conf import settings
from django.core import mail


def mass(title, message, recipient_list):
    mail.send_mass_mail(
        datatuple=((title, message, settings.EMAIL_HOST_USER, (recipient,)) for recipient in recipient_list),
        fail_silently=False
    )
