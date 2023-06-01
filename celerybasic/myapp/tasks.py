from celery import shared_task

@shared_task
def multiply_numbers(x,y):
    result = x*y
    return result

@shared_task
def sqaure_number(x):
    result = x **2
    return result

@shared_task
def add_numbers(x,y):
    result = x + y
    print(result)
    return result