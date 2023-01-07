from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    
    context={
        'form' :form
    }
    return render(request,'users/register.html',context=context)
