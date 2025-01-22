from django.shortcuts import render
from .models import Student

# Create your views here.
def alldata(request):
    x=Student.objects.all()
    print(x)
    y=Student.objects.filter(stu_name='Kratika')
    print(y)  # return multiple object with same name and  no find same so they can return the empty objects
    z=Student.objects.exclude(stu_name='Kratika')
    print(z)  #
    p=Student.objects.filter(stu_name='kratika')
    print(p)  #no find same so they can return the empty objects
    m=Student.objects.order_by("stu_name")
    print(m) #decending
    n=Student.objects.order_by("-stu_name")
    print(n) #assending

