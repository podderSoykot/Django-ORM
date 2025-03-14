from django.shortcuts import render
from .models import Portfolio

def portfolio_view(request):
    portfolio = Portfolio.objects.first()
    return render(request, 'portfolio.html', {'portfolio': portfolio})


