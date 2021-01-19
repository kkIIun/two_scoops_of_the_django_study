from django.shortcuts import render,redirect
from .forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def sign_in_function(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request,username=username,password=password)
            
            if user:
                login(request,user)
                return redirect('index')

    else :
        form = SignInForm()
    return render(request, 'sign.html', { 'form' : form})

def sign_up_function(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                        username = request.POST["username"], 
                        password = request.POST["password"],
                    )
            login(request,user)
            return redirect('index')

    else :
        form = SignUpForm()
    return render(request, 'sign.html', { 'form' : form})

def sing_out_function(request):
    logout(request)
    return redirect('index')