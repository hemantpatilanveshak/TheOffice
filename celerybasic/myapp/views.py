from django.shortcuts import render
from myapp.tasks import multiply_numbers , add_numbers , sqaure_number
from celery import chain
from django.http import HttpResponse

# Create your views here.

def perform_calculation(request):

    # task_result = add_numbers(8,10)
    task_result = add_numbers.delay(20,30)
    result = task_result.get()

    return HttpResponse(f"The final calcuation is {result}")