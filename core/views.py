

from django.shortcuts import render,HttpResponse
# from core.models import Contact
from datetime import datetime
from django.db import models

from django.contrib import messages

# Create your views here.
def index(request):

       
    return render(request,'index.html')  


# Create your views here.
