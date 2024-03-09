

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()


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
            
            # Query the database to find a user with the provided username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            
            # If a user is found and the password matches, log in the user
            if user and check_password(password, user.password):
                login(request, user)
                # Redirect to the homepage or any other desired page
                return redirect('homepage')
            else:
                # Authentication failed
                return render(request, 'users/signin.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = SignInForm()
    return render(request, 'users/signin.html', {'form': form})
