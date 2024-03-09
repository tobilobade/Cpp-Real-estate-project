

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, SignInForm
from django.contrib.auth import authenticate, login


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}.'.format(un))
            return redirect('sign_in')
    else:  # Indentation corrected here
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
    
def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the homepage or any other desired page
                return redirect('homepage')
            else:
                # Authentication failed
                return render(request, 'users/signin.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = SignInForm()
    return render(request, 'users/signin.html', {'form': form})
