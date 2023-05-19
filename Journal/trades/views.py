from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Trades

# Create your views here.
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

import json


def home_page(request, *args, **kwargs):
    if request.method == "GET":
        all_trades = Trades.objects.all()
        context = {"trades": all_trades}
        print(request.method)
        return render(request, "base.html", context=context)


# elif request.method == 'POST' :


def upload_trades(request, *args, **kwargs):
    if request.method == "POST":
        data = json.loads(request.body)
        entry = data.get("entry", "")
        _exit = data.get("exit", "")
        ticker = data.get("ticker")
        side = data.get("side")
        stop_loss = data.get("stop_loss", "")
        take_profit = data.get("take_profit")
        pnl = data.get("pnl", "")
        rr = data.get("rr", "")
        tags = data.get("tags", "")
        comment = data.get("comment", "")
        if entry == "":
            return HttpResponseForbidden("The ENTRY field can not be empty!")
        if ticker == "":
            return HttpResponseForbidden("The TICKER field can not be empty!")

        return redirect("home_page")
