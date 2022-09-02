from django.shortcuts import render,HttpResponse
from .models import employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def view(request):
    emps=employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view.html',context)


def remove(request, emp_id = 0):
    if emp_id:
        try:
            emp=employee.objects.get(id=emp_id)
            emp.delete()       
            return  HttpResponse("employee deleted succesfully...") 
        except request.method=='get':
            return HttpResponse("please enter valid id ")
    emps=employee.objects.all()
    context ={
         'emps' : emps
      }
    return render(request,'rem.html', context)


def filter(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps =employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps=emps.filter(Q(dept__name=dept))

        if role:
            emps=emps.filter(Q(role__name=role))

        context ={
            'emps':emps
         }
        return render(request,'view.html',context)

    elif request.method=='GET':
        return render(request,'filter.html')

    else:
        return HttpResponse("an exception occured")

def add(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salery=int(request.POST['salery'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=employee( first_name=first_name, last_name=last_name,salery=salery,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("employee added succesfully")
    elif request.method=='GET':
        return render(request,'add.html')

    else:
        return HttpResponse("exception is occured")


    