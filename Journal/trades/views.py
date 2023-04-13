from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trade
from .forms import TradeForm
# Create your views here.

def index(request):
    trades = Trade.objects.order_by('entry_time')[:10]
    context = { 'trades' : trades}

    if request.method == 'POST':
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trade created successfully.')
            return redirect('index')
            # do something with the created trade object
        
        return redirect('index')
    else:
        form = TradeForm()

    context['form'] = form
    return render(request, 'index.html',context)



def dashboard(request, *args, **kwargs):
    return render(request, 'dashboard.html')