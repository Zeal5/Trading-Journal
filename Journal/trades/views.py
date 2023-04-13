from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trade
from .forms import TradeForm
# Create your views here.
from django.core.paginator import Paginator

def index(request):
    trades = Trade.objects.order_by('entry_time')
    paginator = Paginator(trades,per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj.has_next)
    context = { 'trades' : trades,
               'page_obj': page_obj}


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
    return render(request, 'dashboard.html',context)



