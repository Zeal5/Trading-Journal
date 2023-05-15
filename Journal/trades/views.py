from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trade
from .forms import TradeForm
# Create your views here.
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
