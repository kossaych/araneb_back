from django.shortcuts import render
from . models import*

# Create your views here.
def index(request):
    context={
        'cours':Cour.objects.all(),
            }
    return render(request,'base.html',context)

def cour(request,id):
    context={
        'parts':Part.objects.filter(cour=int(id))
            }
    return render(request,'cour.html',context)    




def about(request):
    pass