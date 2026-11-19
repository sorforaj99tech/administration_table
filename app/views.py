from django.shortcuts import render, HttpResponse, redirect
from . models import SignUp

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        tech = request.POST.get('tech')
        dept = request.POST.get('dept')
        shift = request.POST.get('shift')
        password = request.POST.get('pass')
        print(name,email,phone,tech,dept,shift,password)
        data = SignUp(username=name, email=email, phone=phone,tech=tech, dept=dept, shift=shift, password=password)
        data.save()
        
        return redirect('data_list')
        
    
    return render(request, 'index.html')

def data(request):
    data = SignUp.objects.all()
    context = {
        'todo':data
    }
    return render(request, 'data.html', context)