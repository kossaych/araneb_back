from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def product(request):
    return render(request,'product/product.html')