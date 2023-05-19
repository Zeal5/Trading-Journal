from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trades

# Create your views here.
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt




def home_page(request,*args, **kwargs):
    if request.method == 'POST':
        all_trades = Trades.objects.all()
        context = {
            "trades" : all_trades }
        print('something')
        return render(request, 'base.html',context=context)



    if request.method == 'GET':
        all_trades = Trades.objects.all()
        context = {
            "trades" : all_trades }
        return render(request, 'base.html',context=context)
    
    # elif request.method == 'POST' :



