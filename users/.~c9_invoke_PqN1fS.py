

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from .forms import UserSignUpForm, SignInForm

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
            # Manually check the database for authentication
            user = User.objects.filter(username=username).first()
            if user is not None and user.check_password(password):
                # Manually set user as authenticated in the session
                login(request, user)
                # Redirect to the homepage or any other desired page
                return redirect('homepage')
            else:
                # Authentication failed
                return render(request, 'users/signin.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = SignInForm()
    return render(request, 'users/signin.html', {'form': form})
