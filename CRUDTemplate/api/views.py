from django.shortcuts import render , redirect
from .models import Employee
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import EmployeeRegistration


# Create your views here.

def viewpage(request):
    return render(request,'api/index.html')

def getEmployee(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp
    }
    return render(request,'api/index.html',context)

def addEmployee(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # address = request.POST.get('address')
        # phone = request.POST.get('phone')

        # emp = Employee(
        #     name = name,
        #     email = email,
        #     address = address,
        #     phone = phone
        # )

        form = EmployeeRegistration(request.POST)


        # emp.save()
        # return render('api/index.html')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/apiview/')
    return render(request,template_name='api/index.html')
    # else:
    #     form = addEmployeeForm()



def delEmployee(request,id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=id)