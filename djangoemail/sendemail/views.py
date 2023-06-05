from django.shortcuts import render
from sendemail import models
from .tasks import send_email_func
from django.http import HttpResponse

# Create your views here.

def send_mail_to_all(request):
    send_email_func.delay()
    return HttpResponse("Mail Sent")