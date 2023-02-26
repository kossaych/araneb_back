from django.shortcuts import render

# Create your views here.
def statistique(request):
    return render(request,'managment/statistiques/statistiques.html')