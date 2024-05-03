from django.shortcuts import render, redirect
from . models import student

# Create your views here.



def homepage(request):
    return render(request,'home.html')


def insert(request):
    if request.method == 'POST':
        sfname = request.POST.get('sf_name')
        slname = request.POST.get('sl_name')
        scourse = request.POST.get('s_course')
        sphone = request.POST.get('s_phone')
        semail = request.POST.get('s_email')
        saddress = request.POST.get('s_address')

        student.objects.create(first_name = sfname, last_name = slname, course = scourse, number = sphone, email = semail, address = saddress)

        return redirect('read')
    

def read(request):
    display = student.objects.all()
    return render(request,'details.html', {'show' : display})


def update(request, student_id):
    students = student.objects.get(id=student_id)
    if request.method == 'POST':
        students.first_name = request.POST.get('sf_name')
        students.last_name = request.POST.get('sl_name')
        students.course = request.POST.get('s_course')
        students.number = request.POST.get('s_phone')
        students.email = request.POST.get('s_email')
        students.address = request.POST.get('s_address')
        students.save()
        
        return redirect('read')
    
    return render(request, 'edit.html', {'students': students})




def delete(request,pk):
    data = student.objects.get(id = pk)
    return render(request,'delete.html',{'value': data})

def sure(request,pk):
    if request.method == 'POST':
        value = student.objects.get(id=pk)
        value.delete()
        return redirect('read')