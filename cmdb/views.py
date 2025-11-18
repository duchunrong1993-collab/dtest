from django.shortcuts import render , HttpResponse,redirect
from .models import host
from .forms import hostForm
def index(request):
    host_list = host.objects.all()
    return render(request, 'main.html',{'host_list':host_list})

def add(request):
    if request.method == 'POST':
        form = hostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = hostForm()
    return render(request, 'add.html',{'form':form})
