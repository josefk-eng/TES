from django.core.mail import send_mail
from django.conf import settings


def sendMail(subject,message,rcpt_list):
    print(f"sender email is {settings.EMAIL_HOST_USER}")
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=rcpt_list,
        fail_silently=True
    )
