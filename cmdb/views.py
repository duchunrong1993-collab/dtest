from django.shortcuts import render , HttpResponse
def index(request):
    return render(request, 'main.html')

def cmdb(request):
    return HttpResponse("this is cmdb")
    
def asset(request,asset_id): 
    return HttpResponse(f"this is asset {asset_id}") 
