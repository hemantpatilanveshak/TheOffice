from . models import Book
from celery import shared_task
from django.core.mail import send_mail
from Books import settings
import pdfkit

@shared_task
def generate_pdf(title,author):
    html = f"<h1>{title}<h1> <h2>{author}<h2>"
    pdfkit.from_string(html,'book_info.pdf')

    


