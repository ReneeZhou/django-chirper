from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import LoginForm, RegistrationForm


def home_notauth(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'home_notauth.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request, request.POST)
        # this is because AuthenticationForm's __init__()
        # takes an extra request arg for custom login like this

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # username = request.POST['username']
            # password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user = user)
                return redirect('home')
        else: 
            return redirect('login')


class UserCreateView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')