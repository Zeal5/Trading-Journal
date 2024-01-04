from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Trades

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from .serializer import TradeSerializer


def home_page(request, *args, **kwargs):
    if request.method == "GET":
        all_trades = Trades.objects.all()
        context = {"trades": all_trades}
        print(request.method)
        return render(request, "base.html", context=context)


# elif request.method == 'POST' :


@api_view(["POST"])
def upload_trades(request, *args, **kwargs):
    # if request.method == "POST":
    #     data = json.loads(request.body)
    #     entry = data.get("entry", "")
    #     _exit = data.get("exit", "")
    #     ticker = data.get("ticker")
    #     side = data.get("side")
    #     stop_loss = data.get("stop_loss", "")
    #     take_profit = data.get("take_profit")
    #     pnl = data.get("pnl", "")
    #     rr = data.get("rr", "")
    #     tags = data.get("tags", "")
    #     comment = data.get("comment", "")
    #     if entry == "":
    #         return HttpResponseForbidden("The ENTRY field can not be empty!")
    #     if ticker == "":
    #         return HttpResponseForbidden("The TICKER field can not be empty!")

    # serializer = TradeSerializer(data=json.loads(request.body))
    serializer = TradeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print("form was valid")
        return Response({"message": "Upload successful"})
    else:
        errors = serializer.errors
        error_message = {}
        for k, v in errors.items():
            error_message[k] = f"{v[0]}"
        print(error_message)

        return Response(error_message, status=400)
