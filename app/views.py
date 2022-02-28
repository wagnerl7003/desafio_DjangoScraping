from django.shortcuts import redirect, render
from app.models import Proxylist
from app.forms import ProxyForm

# Create your views here.

def home(request):
    proxyslist = Proxylist.objects.all()

    context = {
        'proxylist' : proxyslist
    }

    return render(request, 'child/home.html', context)

def InsertProxy(request):
    form = ProxyForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form
    }

    return render(request, 'child/insertproxy.html', context)

def EditProxy(request, proxy_pk):
    proxy = Proxylist.objects.get(pk = proxy_pk)

    form = ProxyForm(request.POST or None, instance = proxy )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form,
        'proxy' : proxy.id
    }

    return render(request, 'child/editproxy.html', context)

def DeleteProxy(request, proxy_pk):
    proxy = Proxylist.objects.get(pk = proxy_pk)
    proxy.delete()
    
    return redirect('home')
