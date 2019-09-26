from django.shortcuts import render
from stock.models import Stock
from stock.serializers import StockSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import StockForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

'''
Class base view
'''
class StockListView(ListView):
    model = Stock   #stock.objects.all()
    template_name = 'stocks/stock_list.html'
    
class StockDetail(DetailView):
    print(">>> StockDetail")
    model = Stock
    template_name = 'stocks/stock_DetailView.html'
    
class StockCreateView(CreateView):
    print("using ModelForm")
    form_class = StockForm
    template_name = 'stocks/stock_create.html'
    
class StockUpdateView(UpdateView):
    form_class = StockForm
    template_name = 'stocks/stock_create.html'
    queryset = Stock.objects.all()
