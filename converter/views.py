from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    content = {
        'amount': 1
    }
    if request.method == 'GET':
        return render(request, 'base.html')
    else:
        amount = request.POST['amount']
        if amount == '':
            content['res'] = 'Please enter some value'
            return render(request, 'base.html', content)
        amount = float(amount)
        content['amount'] = amount

        type = request.POST['type']
        if type == 'Ethereum':
            rate = 351.05
        else:
            rate = 5.25
        content['res'] = '{}: {} * {} = {} USD'.format(type, amount, rate, round(amount*rate, 4))
        return render(request, 'base.html', content)
