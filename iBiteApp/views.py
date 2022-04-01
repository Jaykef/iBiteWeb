from django.shortcuts import render


def index(request):
    return render(request, 'iBiteApp/index.html')


def shop(request):
    return render(request, 'iBiteApp/shop-grid.html')
