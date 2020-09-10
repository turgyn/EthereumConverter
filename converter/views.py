import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse

price = {}

def update_price(request):
    APIURL = 'https://api.coingecko.com/api/v3/simple/price'
    payload = {
        'ids': 'ethereum,ethereum-classic',
        'vs_currencies': 'usd'
    }
    response = requests.get(APIURL, params=payload).json()
    global price
    price['ethereum'] = response['ethereum']['usd']
    price['ethereum_classic'] = response['ethereum-classic']['usd']
    return redirect('home')


def home(request):
    if not price:
        update_price(request)
    content = {
        'amount': 0,
        'price': price
    }
    if request.method == 'GET':
        return render(request, 'base.html', content)
    else:
        amount = request.POST['amount']
        if amount == '':
            amount = 0
        amount = float(amount)
        content['amount'] = amount
        type_ = request.POST['type']
        rate = price[type_.lower()]
        content['text'] = '{}: {} * {} = $'.format(type_, amount, rate)
        content['res'] = round(amount*rate, 4)
        return render(request, 'base.html', content)
