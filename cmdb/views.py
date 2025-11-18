from django.shortcuts import render , HttpResponse,redirect, get_object_or_404
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
    return render(request, 'add.html',{'form':form, 'title': '资产录入'})

def edit(request, pk):
    obj = get_object_or_404(host, pk=pk)
    if request.method == 'POST':
        form = hostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = hostForm(instance=obj)
    return render(request, 'add.html', {'form': form, 'title': '资产编辑'})
