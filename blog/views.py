from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def blog(request):
    return render(request,'blog/blog.html')