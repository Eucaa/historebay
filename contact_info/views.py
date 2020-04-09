from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'about.html')


def tac(request):
    return render(request, 'tac.html')


def pac(request):
    return render(request, 'pac.html')


def contact(request):
    return render(request, 'contact.html')
