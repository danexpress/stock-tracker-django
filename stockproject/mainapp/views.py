from django.shortcuts import render
from django.http import HttpResponse
from yahoo_fin.stock_info import *


# Create your views here.
def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, "mainapp/stockpicker.html", {"stockpicker": stock_picker})


def stockTracker(request):
    stockpicker = request.GET.getlist("stockpicker")
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    for i in stockpicker:
        result = get_quote_table("aapl")
        # data.update({i: result})

    print(result)

    return render(request, "mainapp/stocktracker.html")
