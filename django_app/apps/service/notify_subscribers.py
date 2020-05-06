from apps.core import models
from . import send_mail


def new_book(book):
    send_mail.mass(
        title='We added new book into the Library',
        message=f'Look at the awesome new book "{book.title}"!',
        recipient_list=(subscriber.email for subscriber in models.Subscriber.objects.all())
    )
