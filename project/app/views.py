from django.shortcuts import render
from .models import Student

# Create your views here.
def alldata(request):
    # x=Student.objects.all()
    # print(x)
    # y=Student.objects.filter(stu_name='mohits')
    # print(y)  # return multiple object with same name and  no find same so they can return the empty objects
    # z=Student.objects.exclude(stu_name='mohit')
    # print(z)  #
    # p=Student.objects.filter(stu_name='MOHIT')
    # print(p)  #no find same so they can return the empty objects
    # m=Student.objects.order_by("stu_name")
    # print(m) #decending
    # n=Student.objects.order_by("-stu_name")
    # print(n) #assending
    # a=Student.objects.values_list()
    # print(a)
    # b=Student.objects.values()
    # print(b)
    #-------------return single objects ------------------------
    # c=Student.objects.get(id='1')
    # print(c)
    # m=Student.objects.get(stu_email='Ranu@gmail.com')
    # print(m)
    # #-------------return single objects ------------------------
    # d=Student.objects.first()
    # print(d)
    # e=Student.objects.last()
    # print(e)
    x=Student.objects.all()
    data={
        'data':x.order_by() 
    }
    return render(request,'alldata.html',data)
   
