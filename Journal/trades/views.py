from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt




def home_page(request,*args, **kwargs):
    return render(request, 'base.html')