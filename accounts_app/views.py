from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                # ENVIAR A DASHBOARD
                return redirect('index')  # Replace 'home' with the name of your landing page's URL pattern
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})
