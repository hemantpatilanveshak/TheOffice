from . models import Student
from celery import shared_task
from django.core.mail import send_mail
from djangoemail import settings


@shared_task(bind=True)
def send_email_func(self):
    obj = Student.objects.all()

    for person in obj:
        mail_subject = "Hi This is a test mail from celery"
        message = "Ignore the message Test from Celery "
        to_email =  person.email

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )

    return "Done"