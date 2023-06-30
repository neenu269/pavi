from django.http import HttpResponse
from django.shortcuts import render
from.models import table
# Create your views here.
def demo(request):
     obj=table.objects.all()
     return render(request,"index.html",{'result':obj})