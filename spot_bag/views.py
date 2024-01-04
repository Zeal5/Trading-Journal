from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from .models import SpotBag

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

# from .serializer import TradeSerializer


def home_page(request, *args, **kwargs):
    return HttpResponse("<h1>Hellow</h1>")


# elif request.method == 'POST' :


@api_view(["POST"])
def upload_trades(request, *args, **kwargs):
    pass
