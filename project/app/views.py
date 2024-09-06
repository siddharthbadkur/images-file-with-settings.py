from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    form=ItemInfo()
    if request.method=='POST':
        Data=ItemInfo(request.POST,request.FILES)
        if Data.is_valid():
            Data.save()
            msg="registration succesfully"
            return render(request,'home.html',{'form':form,'msg':msg})
        else:
            msg="PLEASE enter valid data"
            return render(request,'home.html',{'form':form,'msg':msg})
    else:
        return render (request,'home.html',{'form':form})
def show(request):
    form=Studentmodel.objects.all()
    form1=form.values()
    return render(request,'show.html',{'form1':form1})
